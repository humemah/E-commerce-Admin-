from sqlalchemy.orm import Session
from sqlalchemy import func
from models.sales import Sale
from models.product import Product
from datetime import date
from typing import Optional, List

def filtr_sales(db: Session, 
                  fromdate: Optional[date], 
                  todate: Optional[date], product_id: 
                  Optional[int], 
                  category_id: Optional[int]):
    q = db.query(Sale)
       ## datee filterr
    if fromdate:
        q = q.filter(Sale.date_of_sale >= fromdate)
    if todate:
        q = q.filter(Sale.date_of_sale <= todate)


    #### product and cat filter
    if product_id:
        q = q.filter(Sale.product_id == product_id)

    if category_id:
        q = q.join(Product).filter(Product.category_id == category_id)
    return q.all()

def revenue_by_period(db: Session, group_by: str):

    date_format = {
        "daily": "%Y-%m-%d",
        "weekly": "%Y-%u",
        "monthly": "%Y-%m",
        "yearly": "%Y",
    }[group_by]

    rev_data = (
        db.query(func.date_format(Sale.date_of_sale,
                                   date_format).label("Period"),
                func.sum(Sale.total_price).label('revennue'))
        .group_by('Period')
        .order_by('Period')
        .all()
    )
    return rev_data



# reevenue comprsion 
def compare_revenue_periods(db: Session, 
                           from_date1: date,  

    to_date1: date,
    from_date2: date,
    to_date2: date
):
    total1 = (
        db.query(func.sum(Sale.total_price))
        .filter(Sale.date_of_sale.between( from_date1,to_date1 ))
        .scalar()
    ) or 0

    total2 = (
        db.query(func.sum(Sale.total_price))
        .filter(Sale.date_of_sale.between( from_date2, 
                                          to_date2))
        .scalar()
    ) or 0

    return total1, total2
