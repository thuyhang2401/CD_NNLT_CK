from fastapi import FastAPI, HTTPException
from .data_access import DataAccess
from .schema import GlassesSchema
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
sql = DataAccess()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/v1/glasses", response_model=list[GlassesSchema])
def get_all():
    return sql.get_all_glasses()


@app.get("/api/v1/glasses/search", response_model=list[GlassesSchema])
def search_glasses(keyword: str):
    result = sql.search_glasses(keyword)
    if not result:
        raise HTTPException(status_code=404, detail="No glasses found")
    return result


@app.get("/api/v1/glasses/filter", response_model=list[GlassesSchema])
def search_glasses(min: float, max: float):
    result = sql.filter_by_price(min, max)
    if not result:
        raise HTTPException(status_code=404, detail="No glasses found")
    return result

@app.post("/import-glasses")
def import_glasses(items: List[GlassesSchema]):
    success = sql.import_glasses(items)
    if not success:
        raise HTTPException(status_code=400, detail="Failed to import glasses")
    return {"message": "Glasses imported successfully"}
