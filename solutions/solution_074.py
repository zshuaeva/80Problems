# Write a class that meets these requirements.
#
# Name:       BankAccount
#
# Required state:
#    * opening balance, the amount of money in the bank account
#
# Behavior:
#    * get_balance()      # Returns how much is in the bank account
#    * deposit(amount)    # Adds money to the current balance
#    * withdraw(amount)   # Reduces the current balance by amount
#
# Example:
#    account = BankAccount(100)
#
#    print(account.get_balance())  # prints 100
#    account.withdraw(50)
#    print(account.get_balance())  # prints 50
#    account.deposit(120)
#    print(account.get_balance())  # prints 170
#
# There is pseudocode for you to guide you.

# class BankAccount
class BankAccount:                                          # solution
    # method initializer(self, balance)
    def __init__(self, balance):                            # solution
        # self.balance = balance
        self.balance = balance                              # solution

    # method get_balance(self)
    def get_balance(self):                                  # solution
        # returns the balance
        return self.balance                                 # solution

    # method withdraw(self, amount)
    def withdraw(self, amount):                             # solution
        # reduces the balance by the amount
        self.balance -= amount                              # solution

    # method deposit(self, amount)
    def deposit(self, amount):                              # solution
        # increases the balance by the amount
        self.balance += amount                              # solution
