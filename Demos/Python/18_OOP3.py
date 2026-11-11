import importlib
module =importlib.import_module("17_OOP2")
Employee = module.Employee

class Manager(Employee):
    def __init__(self, emp_id, name, salary, department):
        super().__init__(emp_id, name, salary)
        self.department = department

    def display_details(self):
        super().display_details()
        print("Department:", self.department)

    def calculate_bonus(self):
        return self.salary * 0.20  # Managers get a higher bonus percentage

manager1 = Manager(101, "Amit", 80000, "Sales")
manager1.display_details()
print(f"Manager Bonus: {manager1.calculate_bonus()}")