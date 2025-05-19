from pydantic import BaseModel
from datetime import date



class SaleOut(BaseModel):


    id: int
    product_id: int
    quantity_sold: int
    date_of_sale: date

    total_price: float

    class Config:
        orm_mode = True
