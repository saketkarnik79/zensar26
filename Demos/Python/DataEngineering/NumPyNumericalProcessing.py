import numpy as np

# Step 1: Create monthly sales array
sales = np.array([
    12000, 15000, 18000,
    14000, 22000, 25000
])

print("Monthly Sales:")
print(sales)

# Step 2: Basic statistics
print("Total Sales:", np.sum(sales))
print("Average Sales:", np.mean(sales))
print("Maximum Sales:", np.max(sales))
print("Minimum Sales:", np.min(sales))
print("Median Sales:", np.median(sales))
print("Standard Deviation:", np.std(sales))

# Step 3: Apply 10% growth
increased_sales = sales * 1.10

print("\nSales After 10% Growth:")
print(increased_sales)

# Step 4: Filter high-performing months
high_sales = sales[sales > 18000]

print("\nSales Above 18000:")
print(high_sales)

# Step 5: Conditional calculations
performance = np.where(
    sales >= 18000,
    "High",
    "Normal"
)

print("\nSales Performance:")
print(performance)

# Step 6: Reshape array
sales_matrix = sales.reshape(2, 3)

print("\nSales Matrix:")
print(sales_matrix)

# Step 7: Monthly growth rates
growth = np.diff(sales) / sales[:-1] * 100

print("\nMonth-on-Month Growth (%):")
print(np.round(growth, 2))
