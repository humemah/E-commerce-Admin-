from pydantic import BaseModel

class Inventory(BaseModel):
    product_id: int
    quantity: int

class InventoryUpdate(BaseModel):
    ###for put requst
    quantity: int

class InventoryOut(Inventory):
    id: int

    class Config:
        orm_mode = True
