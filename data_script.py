from database import SessionLocal
from models.product import Product
from models.inventory import Inventory
from models.category import Category
from models.sales import Sale
from datetime import date, timedelta
import random

def add_data():
    db: Session = SessionLocal()
    try:
        ############## Clear old data first
        db.query(Sale).delete()
        db.query(Inventory).delete()
        db.query(Product).delete()
        db.query(Category).delete()
        db.commit()

        ################### Addinng  categories
        category1 = Category(name="Fashion")

        category2 = Category(name='axcessories')  
        db.add_all([category1, category2])
        db.commit()

        ################### Addd Products ###########
        products = [
            Product(
                name='Bluetooth Headphones',
                descrption="Noise cAncelling headphones"
                ,  
                price=99.99,
                category_id=category1.id
            ),
            Product(
                name="SmartWatch",
                descrption="Fitness tracke ", 
                price=149.99,
                category_id=category1.id
            ),
            Product(
                name='Tshirt',
                descrption='Cotton , size S',  
                price=19.99,
                category_id=category1.id
            ),
            Product(
                name='Tshirt',
                descrption='Cottonn, size M', 
                price=19.99,
                category_id=category2.id
            )
        ]
        db.add_all(products)
        db.commit()

        ############### Add Inventoryyyyyy
        inventory = [
            Inventory(product_id=products[0].id, quantity=15),
            Inventory(product_id=products[1].id, quantity=7),
            Inventory(product_id=products[2].id, quantity=30)
        ]
        db.add_all(inventory)
        db.commit()

        ###########3         Add Salessssssss
        for _ in range(100):
            product = random.choice(products)
            quantity = random.randint(1, 5)
            price_per_unit = float(product.price)
            date_of_sale = date.today() - timedelta(days=random.randint(0, 90))

            sale = Sale(
                product_id=product.id,
                quantity_sold=quantity,
                total_price=round(quantity * price_per_unit, 2),
                date_of_sale=date_of_sale  
            )
            db.add(sale)

        db.commit()
        print('Dataa seeded successfully')

    finally:
        db.close()

if __name__ == "__main__":
    add_data()
