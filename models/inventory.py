from sqlalchemy import Column, Integer, ForeignKey, TIMESTAMP
from sqlalchemy.sql import func
from database import Base
from sqlalchemy.orm import relationship

class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

##### relationshiip
product = relationship("Product", back_populates="inventory")
inventory = relationship('Inventory', back_populates=" product",  uselist=False)
sales = relationship("Sale", back_populates="product")