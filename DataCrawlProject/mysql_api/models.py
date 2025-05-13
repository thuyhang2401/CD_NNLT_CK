from sqlalchemy import Column, Float, String
from .database import Base

class Glasses(Base):
    __tablename__ = "glasses"
    glasses_id = Column(String(20), primary_key=True, index=True)
    link = Column(String(255))
    glasses_name = Column(String(100))
    brand_name = Column(String(100))
    price = Column(Float)
    img_url = Column(String(255))