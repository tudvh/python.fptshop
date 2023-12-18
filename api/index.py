from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from services import product_service, category_service
from datetime import date

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class IProduct(BaseModel):
    name: str
    category: str
    brand: str
    price: int
    image_url: str


# Get all product
@app.get("/products")
def get_all_products_func(name: str = '', category: str = ''):
    return product_service.get_all(name, category)


# Add list products
@app.post("/products/add-list")
def add_list_products_func(products: list[IProduct] = []):
    return product_service.add_list(products)


# Add product
@app.post("/products/add")
def add_product_func(name: str, category: str, brand: str, price: int, image_url: str):
    return product_service.add(name, category, brand, price, image_url)


# Get list histories
@app.get("/products/histories")
def get_history_func(date_start: date = None, date_end: date = None):
    if date_start is None:
        date_start = '0000-01-01'
    if date_end is None:
        date_end = '9999-12-31'
    return product_service.get_history(date_start, date_end)


# Get list categories
@app.get("/categories")
def get_all_categories_func():
    return category_service.get_all()
