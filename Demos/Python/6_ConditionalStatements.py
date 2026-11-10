# age = int(input("Enter age: "))

# if age >= 18:
#     print("Eligible to Vote")
# else:
#     print("Not Eligible to Vote")

# marks = int(input("Enter marks (0-100): "))

# if marks < 0 or marks > 100:
#     print("Invalid Marks")
# elif marks >= 90:
#     print("Grade A+")
# elif marks >= 75:
#     print("Grade A")
# elif marks >= 60:
#     print("Grade B")
# elif marks >= 40:
#     print("Grade C")
# else:
#     print("Fail")

# age = 30
# salary = 55000
# credit_score = 750

# if age >= 21:
#     if salary >= 30000:
#         if credit_score >= 700:
#             print("Loan Eligible")
#         else:
#             print("Credit Score Too Low")
#     else:
#         print("Insufficient Salary")
# else:
#     print("Age Requirement Not Met")

units = int(input("Enter electricity units: "))

if units < 0:
    print("Invalid Units")
else:
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = (100 * 5) + (units - 100) * 7
    else:
        bill = (100 * 5) + (100 * 7) + (units - 200) * 10

    print("Electricity Bill: Rs.", bill)