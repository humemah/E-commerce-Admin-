# E-commerce-Admin
 FastAPI-based back-end API for an E-commerce Admin Dashboard, 
 providing sales analytics, revenue tracking, and inventory management functionalities.

# Features
- Add Products
- Can Track Inventory levels
- Update inventory 
- Check current stock levels
- Record and Filter sales by product ,category or date range
- revenue comparsion [daily, weekly, monthly, yearly]

# setup instructions
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

# Install Dependencies
pip install -r requirement.txt
Create a file named .env in the project root
DB_HOST=127.0.0.1
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_password_here
DB_NAME=inventory

# Addd Data
python datascript.py

# run
python -m uvicorn main:app --reload

