
def divide_numbers(a, b):
    try:
        result = a / b

    except ZeroDivisionError:
        print("Error: Cannot divide by zero")

    except TypeError:
        print("Error: Invalid data type")

    else:
        print("Division Result:", result)

    finally:
        print("Division operation completed")

divide_numbers(20, 5)
divide_numbers(10, 0)
divide_numbers(10, "abc")
