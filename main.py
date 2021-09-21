from typing import Optional

from fastapi import FastAPI, Path, Query # fastapi랑 Query를 import (클래스)

from pydantic import BaseModel

from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

app = FastAPI() # app이라는 fastapi 인스턴스 생성



@app.get("/") # 경로 동작 데코레이터
async def root(): # async 함수
    return {"message": "Hello World"} # dictionary를 반환 (json 형태)

@app.get("/item/{item_id}") # 자원 경로
async def read_item(item_id : int): # 매개변수를 int로 지정, int가 아닐경우 오류발생
    return {"item_id" : item_id}

@app.get("/models/{model_name}") # 열거형
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"} # dictionary
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}

@app.get("/files/{file_path:path}") # 경로포함 매개변수
async def read_file(file_path: str):
    return {"file_path": file_path}

@app.get("/items/{item_id}")
async def read_items(
    item_id: int = Path(..., title="The ID of the item to get"),
    q: Optional[str] = Query(None, alias="item-query"),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

@app.post("/items/")
async def create_item(item : Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

@app.put("/items/{item_id}")
async def create_item(item_id : int, item: Item):
    return {"item_id":item_id, **item.dict()}

from typing import Optional

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Optional[str] = Query(None, max_length=50)): # min_length로 최소 길이 설정 가능
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:   
        results.update({"q": q})
    return results

#async def read_items(q: Optional[List[str]] = Query(None)): 같이 여러개 넘기기 가능
