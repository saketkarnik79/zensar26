# Employee JSON Processing

import json

employees = [
    {
        "id": 101,
        "name": "Rahul",
        "department": "IT",
        "salary": 50000
    },
    {
        "id": 102,
        "name": "Priya",
        "department": "HR",
        "salary": 60000
    }
]

# Step 1: Write JSON file
with open("employees.json", "w", encoding="utf-8") as file:
    json.dump(employees, file, indent=4)

print("JSON file created")

# Step 2: Read JSON file
with open("employees.json", "r", encoding="utf-8") as file:
    loaded_employees = json.load(file)

# Step 3: Process records
for employee in loaded_employees:
    print(
        employee["name"],
        employee["department"],
        employee["salary"]
    )

# Step 4: Add a new employee
loaded_employees.append({
    "id": 103,
    "name": "Amit",
    "department": "Finance",
    "salary": 55000
})

# Step 5: Save updated JSON
with open("employees.json", "w", encoding="utf-8") as file:
    json.dump(loaded_employees, file, indent=4)

print("Total Employees:", len(loaded_employees))
