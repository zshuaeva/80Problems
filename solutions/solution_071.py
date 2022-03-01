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
# Do it without pseudocode, this time, from memory. Don't look
# at the last one you just wrote unless you really must.


class Employee:                                                     # solution
    def __init__(self, first_name, last_name):                      # solution
        self.first_name = first_name                                # solution
        self.last_name = last_name                                  # solution

    def get_fullname(self):                                         # solution
        return self.first_name + " " + self.last_name               # solution

    def get_email(self):                                            # solution
        name = (self.first_name + "." + self.last_name).lower()     # solution
        return name + "@company.com"                                # solution
