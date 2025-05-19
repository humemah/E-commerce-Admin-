from fastapi import Depends, FastAPI, HTTPException,APIRouter
from sqlalchemy.orm import Session
from database import SessionLocal
from models.inventory import Inventory
from schemas import inventory_schemas as schemas
from models.product import Product
import crud.inventory as crud

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/inventory", response_model=list[schemas.InventoryOut])

def get_inventry(db: Session = Depends(get_db)):
    print(' inventory..')
    return crud.get_inventry(db)



@router.get("/inventory/low-stock", response_model=list[schemas.InventoryOut])
def fetch_lowstock_inventory(db: Session = Depends(get_db)):

    return crud.get_lowstock_inventory(db)


##udate invenotyr
@router.put("/inventory/{product_id}", response_model=schemas.InventoryOut)
def update_inventory(product_id: int, update: schemas.InventoryUpdate, db: Session = Depends(get_db)):
    
    item = crud.update_inventory_quantity(db, product_id, update.quantity)
    if not item:
        raise HTTPException(
            status_code=404, 
            detail='Inventory itemm {product_id} not fond')
    return item
        

