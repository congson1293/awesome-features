from fastapi import FastAPI  # import class FastAPI() từ thư viện fastapi

"""
Create a simple API
Run in terminal 
```
uvicorn main:app --host 0.0.0.0 --port 8000
```
Add --reload if in dev env
"""

app = FastAPI()  # gọi constructor và gán vào biến app


@app.get("/")  # giống flask, khai báo phương thức get và url
async def root():  # do dùng ASGI nên ở đây thêm async, nếu bên thứ 3 không hỗ trợ thì bỏ async đi
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id:int):
    return {"item_id": item_id}

"""
Request Body
"""
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel # import class BaseModel của thư viện pydantic


class Item(BaseModel): # kế thừa từ class Basemodel và khai báo các biến
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item): # khai báo dưới dạng parameter
    return item