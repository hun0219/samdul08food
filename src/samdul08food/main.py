import pickle
import os
from typing import Union
from fastapi import FastAPI

#with open(get_model_path(), "rb") as f:
#    fish_model = pickle.load(f)

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "n08"}

@app.get("/food")
def food(name: str):
    #시간을 구함
    # 음식 이름과 시간을 csv로 저장 -> /code/data/food.csv
    return {"food": name, "time": "2024-09-15 11:12:13"}
