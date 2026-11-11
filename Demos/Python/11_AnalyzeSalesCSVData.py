# Create, Read, & Analyze Sales CSV Data

import csv

sales_data = [
    {"order_id": 101, "product": "Laptop", "amount": 50000},
    {"order_id": 102, "product": "Mouse", "amount": 1000},
    {"order_id": 103, "product": "Keyboard", "amount": 2500},
    {"order_id": 104, "product": "Monitor", "amount": 15000}
]

# Step 1: Write CSV
with open("sales.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["order_id", "product", "amount"]
    )

    writer.writeheader()
    writer.writerows(sales_data)

print("CSV file created")

# Step 2: Read CSV
total_sales = 0

with open("sales.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        amount = int(row["amount"])
        total_sales += amount

        print(row["product"], amount)

# Step 3: Calculate summary
print("Total Sales:", total_sales)
print("Average Sales:", total_sales / len(sales_data))
