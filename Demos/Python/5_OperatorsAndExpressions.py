# Arithmetic operators
# a = 20
# b = 6

# print("Addition:", a + b)
# print("Subtraction:", a - b)
# print("Multiplication:", a * b)
# print("Division:", a / b)
# print("Floor Division:", a // b)
# print("Modulus:", a % b)
# print("Exponent:", a ** b)

# Comparison & Logical Operators
# age = 25
# salary = 50000

# print(age >= 18)
# print(salary == 50000)
# print(age != 30)

# print(age >= 18 and salary >= 30000)
# print(age < 18 or salary > 40000)
# print(not(age > 30))

# Membership & Identity Operators
# courses = ["Python", "Java", "Azure"]

# print("Python" in courses)
# print("C++" not in courses)

# a = [10, 20]
# b = a
# c = [10, 20]

# print(a is b)
# print(a is c)
# print(a == c)

# Salary Calculation Example
basic_salary = 40000

hra = basic_salary * 0.20
da = basic_salary * 0.10
pf = basic_salary * 0.12

gross_salary = basic_salary + hra + da
net_salary = gross_salary - pf

print("Basic Salary:", basic_salary)
print("HRA:", hra)
print("DA:", da)
print("PF Deduction:", pf)
print("Gross Salary:", gross_salary)
print("Net Salary:", net_salary)