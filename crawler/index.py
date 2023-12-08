from fastapi import FastAPI
from crawler import crawl

app = FastAPI()


@app.post("/crawl")
def crawl_func(phone_page: int = 0, laptop_page: int = 0, tablet_page: int = 0):
    return crawl(phone_page, laptop_page, tablet_page)
