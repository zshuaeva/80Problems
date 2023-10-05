# Modify the withdraw method of BankAccount so that the bank
# account can not have a negative balance.
#
# If a person tries to withdraw more than what is in the
# balance, then the method should raise a ValueError.

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        # If the amount is more than what is in
        # the balance, then raise a ValueError
        if amount > self.balance:                   # solution
            raise ValueError                        # solution
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount
