from pydantic import BaseModel
from typing import Optional
from datetime import datetime



class ProductBase(BaseModel):
    ##3 base schmea
    name: str
    descrption: Optional[str] = None
    price: float
    category_id: int

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    ##3 schema for response
    id: int
    created_at: datetime

    class Config:
        orm_mode = True