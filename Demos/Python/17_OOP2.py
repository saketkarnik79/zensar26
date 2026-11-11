# Constructor Example using Employee Management System

class Employee:

    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        return self.salary * 0.10

    def display_details(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Bonus:", self.calculate_bonus())


emp1 = Employee(101, "Rahul", 50000)
emp2 = Employee(102, "Priya", 60000)

emp1.display_details()
print("----------------")
emp2.display_details()