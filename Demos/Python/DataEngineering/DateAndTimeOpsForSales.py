
import pandas as pd

# Step 1: Create sales transactions
sales = pd.DataFrame({
    "OrderID": [101, 102, 103, 104, 105],
    "OrderDate": [
        "2026-11-01 10:30:00",
        "2026-11-01 14:00:00",
        "2026-11-02 09:15:00",
        "2026-11-03 16:45:00",
        "2026-12-01 11:00:00"
    ],
    "DeliveryDate": [
        "2026-11-04",
        "2026-11-05",
        "2026-11-06",
        "2026-11-07",
        "2026-12-05"
    ],
    "Amount": [5000, 3000, 7000, 4000, 6000]
})

# Step 2: Convert to datetime
sales["OrderDate"] = pd.to_datetime(
    sales["OrderDate"]
)

sales["DeliveryDate"] = pd.to_datetime(
    sales["DeliveryDate"]
)

# Step 3: Extract date components
sales["Year"] = sales["OrderDate"].dt.year
sales["Month"] = sales["OrderDate"].dt.month
sales["Day"] = sales["OrderDate"].dt.day

sales["Weekday"] = (
    sales["OrderDate"].dt.day_name()
)

# Step 4: Calculate delivery duration
sales["DeliveryDays"] = (
    sales["DeliveryDate"].dt.normalize() -
    sales["OrderDate"].dt.normalize()
).dt.days

# Step 5: Filter November orders
november_sales = sales[
    (sales["OrderDate"] >= "2026-11-01") &
    (sales["OrderDate"] < "2026-12-01")
]

# Step 6: Daily sales aggregation
daily_sales = sales.groupby(
    sales["OrderDate"].dt.date
)["Amount"].sum().reset_index()

# Step 7: Monthly sales aggregation
monthly_sales = sales.groupby(
    sales["OrderDate"].dt.to_period("M")
)["Amount"].sum().reset_index()

# Step 8: Average delivery duration
average_delivery = sales["DeliveryDays"].mean()

print("Processed Sales:")
print(sales)

print("\nNovember Sales:")
print(november_sales)

print("\nDaily Sales:")
print(daily_sales)

print("\nMonthly Sales:")
print(monthly_sales)

print("\nAverage Delivery Days:", average_delivery)

# Step 9: Save reports
daily_sales.to_csv("daily_sales.csv", index=False)
monthly_sales.to_csv("monthly_sales.csv", index=False)
