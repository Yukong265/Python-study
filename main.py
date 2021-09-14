from fastapi import FastAPI # fastapi를 import (클래스)

app = FastAPI() # app이라는 fastapi 인스턴스 생성


@app.get("/") # 경로 동작 데코레이터
async def root(): # async 함수
    return {"message": "Hello World"} # dictionary를 반환 (json 형태)