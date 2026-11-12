import pandas as pd
import numpy as np

# Step 1: Create raw data
data = {
    "CustomerID": [101, 102, 103, 104, 104, 105],
    "Name": [
        " amit ", "PRIYA", "rahul",
        "Neha", "Neha", "vikas"
    ],
    "Age": [25, np.nan, 30, 28, 28, 35],
    "City": [
        "mumbai", "PUNE", None,
        "Delhi", "Delhi", "MUMBAI"
    ],
    "Salary": [
        "50000", "45000", "60000",
        "55000", "55000", "invalid"
    ]
}

df = pd.DataFrame(data)

print("Raw Data:")
print(df)

# Step 2: Remove duplicate customers
df = df.drop_duplicates(
    subset=["CustomerID"],
    keep="first"
).copy()

# Step 3: Standardize names
df["Name"] = df["Name"].str.strip().str.title()

# Step 4: Standardize city names
df["City"] = (
    df["City"]
    .fillna("Unknown")
    .str.strip()
    .str.title()
)

# Step 5: Convert salary to numeric
df["Salary"] = pd.to_numeric(
    df["Salary"],
    errors="coerce"
)

# Step 6: Handle missing ages
median_age = df["Age"].median()
df["Age"] = df["Age"].fillna(median_age)

# Step 7: Preserve unknown salaries
# Do not invent a salary value
df["SalaryStatus"] = np.where(
    df["Salary"].isna(),
    "Needs Review",
    "Valid"
)

# Step 8: Validate ages
df = df[
    df["Age"].between(18, 100)
].copy()

# Step 9: Create salary categories
df["SalaryCategory"] = np.select(
    [
        df["Salary"] >= 55000,
        df["Salary"] >= 45000
    ],
    [
        "High",
        "Medium"
    ],
    default="Low"
)

df.loc[
    df["Salary"].isna(),
    "SalaryCategory"
] = "Unknown"

# Step 10: Export cleaned data
df.to_csv(
    "cleaned_customers.csv",
    index=False
)

print("\nCleaned Data:")
print(df)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nData Cleaning Completed!")
