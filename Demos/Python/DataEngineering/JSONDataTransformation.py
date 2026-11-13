
import json
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent

INPUT_FILE = BASE_DIR / "orders.json"

# ----------------------------------
# STEP 1: Read JSON
# ----------------------------------

with open(INPUT_FILE, "r", encoding="utf-8") as file:
    data = json.load(file)

orders = data["orders"]

print("Total Orders:", len(orders))

# ----------------------------------
# STEP 2: Flatten Nested JSON
# ----------------------------------

records = []

for order in orders:

    order_id = order["order_id"]
    order_date = order["order_date"]

    customer = order["customer"]

    for item in order["items"]:

        record = {
            "OrderID": order_id,
            "OrderDate": order_date,
            "CustomerID": customer["customer_id"],
            "CustomerName": customer["name"],
            "City": customer["city"],
            "Product": item["product"],
            "Quantity": item["quantity"],
            "UnitPrice": item["price"]
        }

        records.append(record)

df = pd.DataFrame(records)

print("\nFlattened JSON Data:")
print(df)

# ----------------------------------
# STEP 3: Convert Data Types
# ----------------------------------

df["OrderDate"] = pd.to_datetime(
    df["OrderDate"]
)

df["Quantity"] = pd.to_numeric(
    df["Quantity"]
)

df["UnitPrice"] = pd.to_numeric(
    df["UnitPrice"]
)

# ----------------------------------
# STEP 4: Calculate Revenue
# ----------------------------------

df["TotalAmount"] = (
    df["Quantity"] * df["UnitPrice"]
)

# ----------------------------------
# STEP 5: Date Transformations
# ----------------------------------

df["Year"] = df["OrderDate"].dt.year
df["Month"] = df["OrderDate"].dt.month

# ----------------------------------
# STEP 6: Customer Summary
# ----------------------------------

customer_summary = df.groupby(
    ["CustomerID", "CustomerName"]
).agg(
    TotalRevenue=("TotalAmount", "sum"),
    TotalItems=("Quantity", "sum")
).reset_index()

# ----------------------------------
# STEP 7: Product Summary
# ----------------------------------

product_summary = df.groupby(
    "Product"
).agg(
    TotalQuantity=("Quantity", "sum"),
    TotalRevenue=("TotalAmount", "sum")
).reset_index()

# ----------------------------------
# STEP 8: City Summary
# ----------------------------------

city_summary = df.groupby(
    "City"
)["TotalAmount"].sum().reset_index()

city_summary.columns = [
    "City",
    "TotalRevenue"
]

# ----------------------------------
# STEP 9: Export CSV
# ----------------------------------

df.to_csv(
    BASE_DIR / "flattened_orders.csv",
    index=False
)

customer_summary.to_csv(
    BASE_DIR / "customer_summary.csv",
    index=False
)

product_summary.to_csv(
    BASE_DIR / "product_summary.csv",
    index=False
)

# ----------------------------------
# STEP 10: Export Transformed JSON
# ----------------------------------

json_records = df.copy()

json_records["OrderDate"] = (
    json_records["OrderDate"]
    .dt.strftime("%Y-%m-%d")
)

with open(
    BASE_DIR / "transformed_orders.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        json_records.to_dict(orient="records"),
        file,
        indent=4
    )

# ----------------------------------
# STEP 11: Validation
# ----------------------------------

assert len(df) == 5
assert df["TotalAmount"].sum() == 66500

print("\nCustomer Summary:")
print(customer_summary)

print("\nProduct Summary:")
print(product_summary)

print("\nCity Summary:")
print(city_summary)

print("\nTotal Revenue:", df["TotalAmount"].sum())

print("\nJSON Transformation Completed!")
