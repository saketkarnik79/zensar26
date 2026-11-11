# Employee File Management System

from pathlib import Path

file_path = Path("employees.txt")

# Step 1: Write data
with open(file_path, "w", encoding="utf-8") as file:
    file.write("101,Rahul,IT\n")
    file.write("102,Priya,HR\n")
    file.write("103,Amit,Finance\n")

print("File created successfully")

# Step 2: Append data
with open(file_path, "a", encoding="utf-8") as file:
    file.write("104,Neha,Marketing\n")

print("New employee added")

# Step 3: Read entire file
with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()

print("\nAll Employees:")
print(content)

# Step 4: Read line by line
with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        emp_id, name, department = line.strip().split(",")
        print(f"{emp_id} - {name} - {department}")

# Step 5: Check whether file exists
print("File Exists:", file_path.exists())