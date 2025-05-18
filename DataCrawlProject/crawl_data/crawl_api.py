from fastapi import FastAPI
from .crawl import DataCrawling

app = FastAPI()
data_crawling = DataCrawling()


# before crawling start timer
@app.on_event("startup")
def startup():
    data_crawling.timer_crawl()


@app.get("/crawl")
def crawl():
    data_crawling.crawling()
    data = data_crawling.data
    data_crawling.reset_data()
    return data