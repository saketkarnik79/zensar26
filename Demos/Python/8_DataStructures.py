# List

# students = ["Amit", "Rahul", "Priya", "Neha"]

# print(students)
# print(students[0])
# print(students[-1])
# print(students[1:3]) # Slice from index 1 to 3 (not inclusive)

# List Operations
# numbers = [10, 20, 30, 40]

# numbers.append(50)
# print("After Append:", numbers)

# numbers.insert(1, 15)
# print("After Insert:", numbers)

# numbers.remove(30)
# print("After Remove:", numbers)

# numbers.pop()
# print("After Pop:", numbers)

# numbers[0] = 100
# print("After Update:", numbers)

# numbers.sort()
# print("Sorted:", numbers)

# numbers.reverse()
# print("Reversed:", numbers)

# marks = [75, 85, 90, 65, 95]

# print("Total:", sum(marks))
# print("Maximum:", max(marks))
# print("Minimum:", min(marks))
# print("Average:", sum(marks) / len(marks))

# salaries = [35000, 45000, 55000, 30000, 65000]

# high_salary_employees = []

# for salary in salaries:
#     if salary >= 45000:
#         high_salary_employees.append(salary)

# print("All Salaries:", salaries)
# print("High Salaries:", high_salary_employees)
# print("Total Payroll:", sum(salaries))
# print("Average Salary:", sum(salaries) / len(salaries))

# Tuples
# courses = ("Python", "Java", "Azure", "Python")

# print(courses)
# print(courses[0])
# print(courses[-1])
# print(courses.count("Python"))
# print(courses.index("Azure"))

# employee = (101, "Rahul", 45000)

# employee_id, name, salary = employee # Unpacking the tuple into individual variables (Also known as destructuring assignment)

# print("Employee ID:", employee_id)
# print("Name:", name)
# print("Salary:", salary)

# def calculate(a, b):
#     addition = a + b
#     multiplication = a * b

#     return addition, multiplication

# result = calculate(10, 5)

# print("Result:", result)

# add, multiply = result

# print("Addition:", add)
# print("Multiplication:", multiply)

# Sets
# numbers = {10, 20, 30, 20, 40, 10}

# print(sorted(numbers))

# numbers.add(50)
# print(sorted(numbers))

# numbers.remove(20)
# print(sorted(numbers))

# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}

# print("Union:", sorted(a | b))
# print("Intersection:", sorted(a & b))
# print("Difference:", sorted(a - b))
# print("Symmetric Difference:", sorted(a ^ b))

# student_ids = [101, 102, 103, 101, 104, 102]

# unique_ids = sorted(set(student_ids))

# print("Original IDs:", student_ids)
# print("Unique IDs:", unique_ids)
# print("Total Unique Students:", len(unique_ids))

# Dictionary
# employee = {
#     "id": 101,
#     "name": "Rahul",
#     "department": "IT",
#     "salary": 50000
# }

# print(employee)
# print(employee["name"])
# print(employee.get("department"))

# student = {
#     "id": 101,
#     "name": "Amit",
#     "marks": 85
# }

# student["marks"] = 90
# student["grade"] = "A"

# print("After Update:", student)

# student.pop("grade")

# print("After Remove:", student)

# print("Keys:", list(student.keys()))
# print("Values:", list(student.values()))

# employee = {
#     "name": "Priya",
#     "department": "HR",
#     "salary": 45000
# }

# for key, value in employee.items():
#     print(key, ":", value)

# employees = {
#     101: {
#         "name": "Amit",
#         "department": "IT",
#         "salary": 50000
#     },
#     102: {
#         "name": "Priya",
#         "department": "HR",
#         "salary": 45000
#     },
#     103: {
#         "name": "Rahul",
#         "department": "Finance",
#         "salary": 60000
#     }
# }

# for emp_id, details in employees.items():
#     print("Employee ID:", emp_id)
#     print("Name:", details["name"])
#     print("Department:", details["department"])
#     print("Salary:", details["salary"])
#     print("-------------------")

# List Comprehensions
# new_list = [expression for item in iterable if condition]
# squares = []

# for i in range(1, 6):
#     squares.append(i ** 2)

# print(squares)

# Using List Comprehension
# squares = [i ** 2 for i in range(1, 6)]
# print(squares)

# numbers = [10, 15, 20, 25, 30, 35]
# even_numbers = [n for n in numbers if n % 2 == 0]
# odd_numbers = [n for n in numbers if n % 2 != 0]
# print(even_numbers)
# print(odd_numbers)

# marks = [35, 60, 75, 30, 90]
# results = ["Pass" if mark >= 40 else "Fail" for mark in marks]
# print(results)

# salaries = [30000, 40000, 50000, 60000]
# updated_salaries = [
#     salary * 1.10
#     for salary in salaries
# ]
# print("Original Salaries:", salaries)
# print("Updated Salaries:", updated_salaries)

# Dictionary Comprehensions
# new_dict = {key_expression: value_expression for item in iterable}
# squares = {n: n ** 2 for n in range(1, 6)}
# print(squares)

# students = {
#     "Amit": 85,
#     "Rahul": 35,
#     "Priya": 92,
#     "Neha": 55
# }
# passed_students = {
#     name: marks
#     for name, marks in students.items()
#     if marks >= 40
# }

# print(passed_students)

# names = ["Amit", "Priya", "Rahul"]
# marks = [85, 90, 75]

# student_marks = {
#     name: mark
#     for name, mark in zip(names, marks)
# }

# print(student_marks)

employees = {
    "Amit": 40000,
    "Priya": 50000,
    "Rahul": 60000
}

updated_salaries = {
    name: round(salary * 1.10)
    for name, salary in employees.items()
}

print(updated_salaries)