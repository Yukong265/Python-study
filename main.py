from fastapi import FastAPI # fastapi를 import (클래스)

from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

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