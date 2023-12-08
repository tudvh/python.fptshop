from fastapi import FastAPI
from pydantic import BaseModel
import api

app = FastAPI()


class IProduct(BaseModel):
    name: str
    category: str
    brand: str
    price: int
    images_url: str


@app.get("/get-all")
def get_all_func(name: str = '', category: str = ''):
    return api.get_all(name, category)


@app.post("/add-list")
def add_list_func(products: list[IProduct] = []):
    return api.add_list(products)


@app.post("/add")
def add_func(name: str, category: str, brand: str, price: int, images_url: str):
    return api.add(name, category, brand, price, images_url)
