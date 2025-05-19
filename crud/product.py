from sqlalchemy.orm import Session
from models.product import Product
from schemas.product_schemas import ProductCreate


######## product registatiomn

def new_product(db: Session, product: ProductCreate):
   
    db_product = Product(
        name=product.name,
        descrption=product.descrption,  
        price=product.price,
        category_id=product.category_id
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product
