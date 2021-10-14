from fastapi import FastAPI, File, Form, UploadFile
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.post("/files/")
async def create_file(
    file: bytes = File(...), fileb: UploadFile = File(...), token: str = Form(...)
):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type
    }

@app.get("/")
async def main():
    content = """
<body>
<form action="/files/" method="post">
<input name="files" type="file">
<input type="submit">
</form>

</body>
    """
    return HTMLResponse(content=content)