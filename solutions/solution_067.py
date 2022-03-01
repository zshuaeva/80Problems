# Write a class that meets these requirements.
#
# Name:       Employee
#
# Required state:
#    * first name, a string
#    * last name, a string
#
# Behavior:
#    * get_fullname: should return "«first name» «last name»"
#    * get_email:    should return "«first name».«last name»@company.com"
#                    all in lowercase letters
#
# Example:
#    employee = Employee("Duska", "Ruzicka")
#
#    print(employee.get_fullname())  # prints "Duska Ruzicka"
#    print(employee.get_email())     # prints "duska.ruzicka@company.com"
#
# You may want to look at the ".lower()" method for strings to
# help with this code.
#
# There is pseudocode availabe for you to guide you


# class Employee
class Employee:                                                     # solution
    # method initializer method with required state
    # parameters first name and last name
    def __init__(self, first_name, last_name):                      # solution
        # set self.first_name = first_name
        self.first_name = first_name                                # solution
        # set self.last_name = last_name
        self.last_name = last_name                                  # solution

    # method get_fullname(self)
    def get_fullname(self):                                         # solution
        # returns self.first_name + " " + self.last_name
        return self.first_name + " " + self.last_name               # solution

    # method get_email(self)
    def get_email(self):                                            # solution
        # returns self.first_name.lower() + "." + self.last_name.lower()
        #         + "@company.com"
        name = (self.first_name + "." + self.last_name).lower()     # solution
        return name + "@company.com"                                # solution
