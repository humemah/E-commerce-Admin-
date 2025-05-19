from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas import sales_schemas as schemas
from typing import  List
from datetime import date

from crud import sales as sales_crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/sales", response_model=List[schemas.SaleOut])

def get_sales(
     fromdate=None,
    todate=None,
    product_id=None,
    category_id= None,
    db=Depends(get_db)
):
    print('SAles Filtet', fromdate, todate, product_id, category_id)

    return sales_crud.filtr_sales(db, fromdate, todate, product_id, category_id)

@router.get("/sales/revenue")


def get_revenue(

    group_by: str = Query("daily", enum=["daily", "weekly", "monthly", "yearly"]),
    db: Session = Depends(get_db),
):
    revenues = sales_crud.revenue_by_period(db, group_by)
    result = []
    for r in revenues:
        result.append({"period": r[0], "revenue": float(r[1])})
    return result

@router.get("/sales/compare")
def compare_rev(from_date1: date, to_date1: date, from_date2: date, to_date2: date, 
                db=Depends(get_db)):
    revv1, revv2 = sales_crud.compare_revenue_periods(db, 
                                                         from_date1, to_date1,  
        from_date2, to_date2
                                                              )
    return {
        "first_period": {'start': from_date1, 'End': to_date1, "revenue": float(revv1)},

        "Seecond_period": {'start': from_date2, 'End': to_date2, "revenue": float(revv2)},
    }