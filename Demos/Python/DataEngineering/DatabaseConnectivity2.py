
import pandas as pd

from sqlalchemy import create_engine, text

# Step 1: Create database engine
engine = create_engine(
    "sqlite:///sales_database.db"
)

# Step 2: Create sales dataset
sales = pd.DataFrame({
    "OrderID": [101, 102, 103, 104],
    "Customer": ["Amit", "Priya", "Rahul", "Neha"],
    "Amount": [5000, 3000, 7000, 4000]
})

# Step 3: Load DataFrame into SQL database
with engine.begin() as connection:
    sales.to_sql(
        "Sales",
        connection,
        if_exists="replace",
        index=False
    )

print("Sales Data Loaded Successfully!")

# Step 4: Read database records
with engine.connect() as connection:
    result = pd.read_sql_query(
        text("SELECT * FROM Sales"),
        connection
    )

print("\nSales Records:")
print(result)

# Step 5: Run aggregation query
query = text("""
    SELECT
        COUNT(*) AS TotalOrders,
        SUM(Amount) AS TotalRevenue,
        AVG(Amount) AS AverageOrderValue
    FROM Sales
""")

with engine.connect() as connection:
    summary = pd.read_sql_query(
        query,
        connection
    )

print("\nSales Summary:")
print(summary)

# Step 6: Release connections
engine.dispose()
