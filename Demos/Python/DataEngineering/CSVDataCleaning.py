
from pathlib import Path
import pandas as pd
import numpy as np

BASE_DIR = Path(__file__).resolve().parent
print (f"Base Directory: {BASE_DIR}")
INPUT_FILE = BASE_DIR / "employees.csv"
OUTPUT_FILE = BASE_DIR / "cleaned_employees.csv"
REJECTED_FILE = BASE_DIR / "rejected_employees.csv"
SUMMARY_FILE = BASE_DIR / "department_summary.csv"

# ----------------------------------
# STEP 1: Extract Data
# ----------------------------------

df = pd.read_csv(INPUT_FILE)

print("Original Dataset:")
print(df)

print("\nDataset Shape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

# ----------------------------------
# STEP 2: Remove Duplicates
# ----------------------------------

df = df.drop_duplicates(
    subset=["EmployeeID"],
    keep="first"
).copy()

print("\nRecords After Deduplication:", len(df))

# ----------------------------------
# STEP 3: Standardize Text
# ----------------------------------

df["Name"] = (
    df["Name"]
    .astype("string")
    .str.strip()
    .str.title()
)

df["Department"] = (
    df["Department"]
    .astype("string")
    .str.strip()
    .str.upper()
    .fillna("UNKNOWN")
)

df["Department"] = df["Department"].replace(
    "", "UNKNOWN"
)

# ----------------------------------
# STEP 4: Convert Data Types
# ----------------------------------

df["Age"] = pd.to_numeric(
    df["Age"],
    errors="coerce"
)

df["Salary"] = pd.to_numeric(
    df["Salary"],
    errors="coerce"
)

# ----------------------------------
# STEP 5: Handle Missing Ages
# ----------------------------------

valid_age_mask = df["Age"].between(18, 65)

median_age = df.loc[
    valid_age_mask, "Age"
].median()

df["Age"] = df["Age"].fillna(median_age)

# ----------------------------------
# STEP 6: Validate Records
# ----------------------------------

invalid_age = ~df["Age"].between(18, 65)

invalid_salary = (
    df["Salary"].isna() |
    (df["Salary"] <= 0)
)

invalid_name = (
    df["Name"].isna() |
    df["Name"].eq("")
).fillna(True)

invalid_mask = (
    invalid_age |
    invalid_salary |
    invalid_name
)

# Save rejected records
rejected = df.loc[invalid_mask].copy()

rejected["RejectionReason"] = np.select(
    [
        invalid_age.loc[rejected.index],
        invalid_salary.loc[rejected.index],
        invalid_name.loc[rejected.index]
    ],
    [
        "Invalid Age",
        "Invalid Salary",
        "Invalid Name"
    ],
    default="Unknown"
)

rejected.to_csv(
    REJECTED_FILE,
    index=False
)

# Keep valid records
cleaned = df.loc[~invalid_mask].copy()

# ----------------------------------
# STEP 7: Transform Data
# ----------------------------------

cleaned["Bonus"] = (
    cleaned["Salary"] * 0.10
).round(2)

cleaned["TotalCompensation"] = (
    cleaned["Salary"] + cleaned["Bonus"]
)

cleaned["SalaryCategory"] = np.select(
    [
        cleaned["Salary"] >= 55000,
        cleaned["Salary"] >= 45000
    ],
    [
        "High",
        "Medium"
    ],
    default="Low"
)

cleaned["Age"] = cleaned["Age"].astype(int)

# ----------------------------------
# STEP 8: Department Summary
# ----------------------------------

summary = cleaned.groupby(
    "Department"
).agg(
    EmployeeCount=("EmployeeID", "count"),
    AverageSalary=("Salary", "mean"),
    TotalSalary=("Salary", "sum")
).reset_index()

summary["AverageSalary"] = (
    summary["AverageSalary"].round(2)
)

# ----------------------------------
# STEP 9: Export Files
# ----------------------------------

cleaned.to_csv(
    OUTPUT_FILE,
    index=False
)

summary.to_csv(
    SUMMARY_FILE,
    index=False
)

# ----------------------------------
# STEP 10: Validate Results
# ----------------------------------

assert cleaned["EmployeeID"].is_unique
assert cleaned["Salary"].notna().all()
assert cleaned["Age"].between(18, 65).all()
assert len(cleaned) == 6
assert len(rejected) == 3

print("\nCleaned Employee Records:")
print(cleaned.to_string(index=False))

print("\nRejected Records:")
print(rejected.to_string(index=False))

print("\nDepartment Summary:")
print(summary.to_string(index=False))

print("\nCSV Cleaning Lab Completed!")
