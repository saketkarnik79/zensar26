# Encapsulation using Bank Account Example

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder # public variable
        self.__balance = balance  # Private variable

    # Public method to check balance
    def get_balance(self):
        return self.__balance

    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: Rs. {amount}")
        else:
            print("Invalid deposit amount")

    # Public method to withdraw money
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: Rs. {amount}")
        else:
            print("Insufficient balance")

    # Public method to display account details
    def display_details(self):
        print("Account Holder:", self.account_holder)
        print("Current Balance:", self.__balance)


# Create an object
account1 = BankAccount("Amit", 50000)

# Display initial account details
account1.display_details()

# Deposit money
account1.deposit(10000)

# Withdraw money
account1.withdraw(20000)

# Check balance
print("Available Balance:", account1.get_balance())

# Attempt to withdraw more than available balance
account1.withdraw(50000)

# Display final account details
account1.display_details()

# print("Available Balance:", account1.__balance)  # This will raise an AttributeError since __balance is private
print("Account Holder:", account1.account_holder)