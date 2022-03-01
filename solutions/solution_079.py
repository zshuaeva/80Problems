# Write a class that meets these requirements.
#
# Name:       ReceiptItem
#
# Required state:
#    * quantity, the amount of the item bought
#    * price, the amount each one of the things cost
#
# Behavior:
#    * get_total()          # Returns the quantity * price
#
# Example:
#    item = ReceiptItem(10, 3.45)
#
#    print(item.get_total())    # Prints 34.5

class ReceiptItem:                              # solution
    def __init__(self, quantity, price):        # solution
        self.quantity = quantity                # solution
        self.price = price                      # solution

    def get_total(self):                        # solution
        return self.quantity * self.price       # solution
