# Write a class that meets these requirements.
#
# Name:       Circle
#
# Required state:
#    * radius, a non-negative value
#
# Behavior:
#    * calculate_perimeter()  # Returns the length of the perimater of the circle
#    * calculate_area()       # Returns the area of the circle
#
# Example:
#    circle = Circle(10)
#
#    print(circle.calculate_perimeter())  # Prints 62.83185307179586
#    print(circle.calculate_area())       # Prints 314.1592653589793
#
# There is pseudocode for you to guide you.

import math

# class Circle
class Circle:                                       # solution
    # method initializer with radius
    def __init__(self, radius):                     # solution
        # if radius is less than 0
        if radius < 0:                              # solution
            # raise ValueError
            raise ValueError                        # solution
        # self.radius = radius
        self.radius = radius                        # solution

    # method calculate_perimeter(self)
    def calculate_perimeter(self):                  # solution
        # returns 2 * math.pi * self.radius
        return 2 * math.pi * self.radius            # solution

    # method calculate_area(self)
    def calculate_area(self):                       # solution
        # returns math.pi * (self.radius squared)
        return math.pi * pow(self.radius, 2)        # solution
