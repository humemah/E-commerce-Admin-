from sqlalchemy import Column, Integer, ForeignKey, DECIMAL, Date
from database import Base
from sqlalchemy.orm import relationship

class Sale(Base):
    
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column( Integer, ForeignKey('products.id'),  
                        nullable=False)
    quantity_sold = Column(Integer, nullable=False)
    date_of_sale = Column(  'sale_date', Date,nullable=False)
    total_price =  Column(DECIMAL(10, 2),  nullable=False)

###3# relationshiip
product = relationship("Product", back_populates="sales")