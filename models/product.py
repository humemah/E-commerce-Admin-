from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey,  TIMESTAMP
from database import Base
from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    descrption = Column("description",String)

    category_id = Column(Integer , ForeignKey('categories.id'))
    price = Column(DECIMAL(10, 2), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
  

    category = relationship("Category", back_populates="products")
