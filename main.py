from fastapi import FastAPI
from dotenv import load_dotenv
from models.category import Category
from database import engine, Base
from routers import product_route  
from routers import inventory_route
from models import product, inventory
from routers import sales_route


app = FastAPI()

Base.metadata.create_all(bind=engine)

# routers
app.include_router(product_route.router)

app.include_router(inventory_route.router)
app.include_router(sales_route.router)

@app.get("/")
def root():
    return {"messagge": "Hello World"}


