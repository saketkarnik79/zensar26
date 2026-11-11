# # Function without parameters and without return value
# def greet():
#     print("Hello! Welcome to the program.")

# # Function with parameters and without return value
# def employee_details(emp_id, name, department):
#     print(f"Employee ID: {emp_id}")
#     print(f"Name: {name}")
#     print(f"Department: {department}")

# # Function with parameters and with return value
# def calculate_salary(basic_salary, bonus, hra):
#     gross_salary = basic_salary + bonus + hra
#     return gross_salary

# # Function with default parameters
# def calculate_tax(salary, tax_rate=0.10):
#     tax_amount = salary * tax_rate
#     net_salary = salary - tax_amount
#     return net_salary

# # Function with variable number of arguments
# def sum(*args):
#     total = 0
#     for n in args:
#         total += n
#     return total

# # Function with variable number of keyword arguments
# def display_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# # Function returning multiple values
# def salary_summary(gross_salary, tax_rate=0.10):
#     tax_amount = gross_salary * tax_rate
#     net_salary = gross_salary - tax_amount
#     return gross_salary, tax_amount, net_salary

# # Main Program to demonstrate the functions
# if __name__ == "__main__":
#     greet()
    
#     print("\nEmployee Details:")
#     employee_details(emp_id=101, name="John Doe", department="Finance")
    
#     gross_salary = calculate_salary(basic_salary=50000, bonus=5000, hra=2000)
#     print(f"\nGross Salary: {gross_salary}")
    
#     net_salary = calculate_tax(salary=gross_salary)
#     print(f"Net Salary after Tax: {net_salary}")
    
#     total_sum = sum(10, 20, 30, 40)
#     print(f"\nTotal Sum: {total_sum}")
    
#     print("\nDisplay Info:")
#     display_info(Name="Alice", Age=30, Position="Manager")
    
#     gross, tax, net = salary_summary(gross_salary=gross_salary, tax_rate=0.15)
#     print(f"\nSalary Summary:\nGross Salary: {gross}\nTax Amount: {tax}\nNet Salary: {net}")

# Lambda Functions demos

# # Square of a number
# square = lambda x: x * x

# # Addition
# add = lambda a, b: a + b

# # Check even or odd
# check_even = lambda n: n % 2 == 0

# # Calculate salary bonus
# bonus = lambda salary: salary * 0.10

# print("Square:", square(5))
# print("Addition:", add(10, 20))
# print("Is Even:", check_even(8))
# print("Bonus:", bonus(50000))

# # Sorting Employee Records Using Lambda
# employees = [
#     {"name": "Rahul", "salary": 50000},
#     {"name": "Amit", "salary": 70000},
#     {"name": "Priya", "salary": 60000}
# ]

# sorted_employees = sorted(
#     employees,
#     key=lambda emp: emp["salary"],
#     reverse=True
# )

# for emp in sorted_employees:
#     print(emp["name"], emp["salary"])

# Using map(), filter(), and reduce() with Lambda Functions
# Sales data processing example

from functools import reduce

sales = [1000, 2500, 3000, 1500, 4000]

# MAP: Apply 10% discount
discounted_sales = list(
    map(lambda amount: amount * 0.90, sales)
)

# FILTER: Sales greater than 2000
high_sales = list(
    filter(lambda amount: amount > 2000, sales)
)

# REDUCE: Calculate total sales
total_sales = reduce(
    lambda a, b: a + b,
    sales,
    0
)

# Combining map, filter and reduce
high_value_sales = filter(
    lambda amount: amount > 2000,
    sales
)

discounted_high_sales = map(
    lambda amount: amount * 0.90,
    high_value_sales
)

final_total = reduce(
    lambda a, b: a + b,
    discounted_high_sales,
    0
)

print("Original Sales:", sales)
print("Discounted Sales:", discounted_sales)
print("High Sales:", high_sales)
print("Total Sales:", total_sales)
print("Final Total:", final_total)
