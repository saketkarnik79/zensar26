import pandas as pd

sales = pd.DataFrame({
    "OrderID": [1, 2, 3, 4, 5],
    "Customer": [
        "Amit", "Priya", "Amit",
        "Rahul", "Priya"
    ],
    "Product": [
        "Laptop", "Mouse", "Keyboard",
        "Laptop", "Mouse"
    ],
    "Quantity": [1, 2, 3, 1, 4],
    "UnitPrice": [50000, 500, 1000, 50000, 500]
})

# Calculate total amount
sales["TotalAmount"] = (
    sales["Quantity"] * sales["UnitPrice"]
)

# Apply discount rules
sales["DiscountRate"] = 0.05

sales["DiscountAmount"] = (
    sales["TotalAmount"] *
    sales["DiscountRate"]
)

sales["NetAmount"] = (
    sales["TotalAmount"] -
    sales["DiscountAmount"]
)

# Customer-wise revenue
customer_summary = sales.groupby(
    "Customer"
)["NetAmount"].sum().reset_index()

# Product-wise revenue
product_summary = sales.groupby(
    "Product"
)["NetAmount"].sum().reset_index()

# Pivot table
pivot = sales.pivot_table(
    index="Customer",
    columns="Product",
    values="NetAmount",
    aggfunc="sum",
    fill_value=0
)

print("Transformed Sales:")
print(sales)

print("\nCustomer Summary:")
print(customer_summary)

print("\nProduct Summary:")
print(product_summary)

print("\nPivot Table:")
print(pivot)

sales.to_csv(
    "transformed_sales.csv",
    index=False
)
