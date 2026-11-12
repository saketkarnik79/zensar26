import pandas as pd

customers = pd.DataFrame({
    "CustomerID": [1, 2, 3],
    "CustomerName": ["Amit", "Priya", "Rahul"],
    "City": ["Mumbai", "Pune", "Delhi"]
})

orders = pd.DataFrame({
    "OrderID": [101, 102, 103, 104],
    "CustomerID": [1, 2, 1, 3],
    "Amount": [5000, 3000, 7000, 4000]
})

# Inner join
merged_df = pd.merge(
    orders,
    customers,
    on="CustomerID",
    how="inner",
    validate="many_to_one"
)

print("Merged Customer Orders:")
print(merged_df)

# Customer-wise total sales
customer_sales = merged_df.groupby(
    "CustomerName"
)["Amount"].sum().reset_index()

print("\nCustomer-Wise Sales:")
print(customer_sales)
