# Custom exceptions in Python allow you to create your own error types that can be raised and caught in your code. This can be useful for handling specific error conditions in a more meaningful way.

class InvalidSalaryError(Exception):
    pass

def process_salary(salary):
    if salary < 0:
        raise InvalidSalaryError(
            "Salary cannot be negative"
        )

    return salary * 1.10

try:
    updated_salary = process_salary(-5000)
    print("Updated Salary:", updated_salary)

except InvalidSalaryError as error:
    print("Validation Error:", error)