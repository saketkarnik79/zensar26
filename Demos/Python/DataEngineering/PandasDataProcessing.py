import pandas as pd

# Step 1: Create employee data
employees = {
    "EmployeeID": [101, 102, 103, 104, 105],
    "Name": ["Amit", "Priya", "Rahul", "Neha", "Vikas"],
    "Department": ["IT", "HR", "Finance", "IT", "HR"],
    "Salary": [50000, 45000, 60000, 55000, 48000]
}

# Step 2: Create DataFrame
df = pd.DataFrame(employees)

print("Original Employee Data:")
print(df)

# Step 3: Inspect dataset
print("\nFirst 3 Records:")
print(df.head(3))

print("\nData Types:")
print(df.dtypes)

print("\nStatistical Summary:")
print(df.describe())

# Step 4: Filter employees
high_salary = df[df["Salary"] > 50000]

print("\nEmployees Earning Above 50000:")
print(high_salary)

# Step 5: Add calculated column
df["Bonus"] = df["Salary"] * 0.10
df["TotalSalary"] = df["Salary"] + df["Bonus"]

print("\nEmployees With Bonus:")
print(df)

# Step 6: Group by department
department_summary = df.groupby(
    "Department"
).agg(
    TotalEmployees=("EmployeeID", "count"),
    AverageSalary=("Salary", "mean"),
    TotalSalary=("Salary", "sum")
).reset_index()

print("\nDepartment Summary:")
print(department_summary)

# Step 7: Sort employees
sorted_df = df.sort_values(
    by="Salary",
    ascending=False
)

print("\nEmployees Sorted By Salary:")
print(sorted_df)

# Step 8: Export to CSV
df.to_csv("employees_processed.csv", index=False)

department_summary.to_csv(
    "department_summary.csv",
    index=False
)

print("\nFiles Created Successfully!")
