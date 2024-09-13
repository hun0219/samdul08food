import os
from typing import Union
from fastapi import FastAPI
import datetime
from fastapi.middleware.cors import CORSMiddleware

#with open(get_model_path(), "rb") as f:
#    fish_model = pickle.load(f)

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8899",
    "https://samdul08food-1.web.app",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "n08"}

@app.get("/food")
def food(name: str):
    # 시간을 구함
    # 음식 이름과 시간을 csv로 저장 -> /code/data/food.csv
    # DB 저장
    dt = datetime.datetime.now().strftime('%Y.%m.%d - %H:%M:%S')
    home_path = os.path.expanduser('~')
    path = f"{home_path}/code/data"
    # 폴더 만들기 있으면 패쓰
    os.makedirs(path,exist_ok=True)
    with open(f"{path}/food.csv","a") as f:
        f.write(f"{dt},{name}\n")
    return {"food": name, "time": dt}
