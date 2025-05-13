from pydantic import BaseModel

class GlassesSchema(BaseModel):
    glasses_id: str
    link: str
    glasses_name: str
    brand_name: str
    price: float
    img_url: str

    class Config:
        from_attributes = True