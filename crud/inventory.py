from sqlalchemy.orm import Session
from models.inventory import Inventory



def get_inventry(db: Session):
    return db.query(Inventory).all()

def get_lowstock_inventory(db: Session):

    return db.query(Inventory).filter(Inventory.quantity < 10).all()

def update_inventory_quantity(db: Session, product_id: int, quantity: int):

    itemm = db.query(Inventory).filter(Inventory.product_id == product_id).first()
    if not itemm:
        return None
    itemm.quantity = quantity
    db.commit()
    db.refresh(itemm)

    return itemm
