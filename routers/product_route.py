from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas import product_schemas as schemas
from crud import product as crud_product  

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/product", response_model=schemas.Product, status_code=201)
def Add_products(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    try:
        return crud_product.new_product(db, product)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
