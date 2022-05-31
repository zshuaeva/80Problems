# Write four classes that meet these requirements.
#
# Name:       Animal
#
# Required state:
#    * number_of_legs, the number of legs the animal has
#    * primary_color, the primary color of the animal
#
# Behavior:
#    * describe()       # Returns a string that describes that animal
#                         in the format
#                                self.__class__.__name__
#                                + " has "
#                                + str(self.number_of_legs)
#                                + " legs and is primarily "
#                                + self.primary_color
#
#
# Name:       Dog, inherits from Animal
#
# Required state:       inherited from Animal
#
# Behavior:
#    * speak()          # Returns the string "Bark!"
#
#
#
# Name:       Cat, inherits from Animal
#
# Required state:       inherited from Animal
#
# Behavior:
#    * speak()          # Returns the string "Miao!"
#
#
#
# Name:       Snake, inherits from Animal
#
# Required state:       inherited from Animal
#
# Behavior:
#    * speak()          # Returns the string "Sssssss!"


class Animal:                                               # solution
    def __init__(self, number_of_legs, primary_color):      # solution
        self.number_of_legs = number_of_legs                # solution
        self.primary_color = primary_color                  # solution
                                                            # solution
    def describe(self):                                     # solution
        return (                                            # solution
            self.__class__.__name__                         # solution
            + " has "                                       # solution
            + str(self.number_of_legs)                      # solution
            + " legs and is primarily "                     # solution
            + self.primary_color                            # solution
        )                                                   # solution
                                                            # solution
                                                            # solution
class Dog(Animal):                                          # solution
    def speak(self):                                        # solution
        return "Bark!"                                      # solution
                                                            # solution
                                                            # solution
class Cat(Animal):                                          # solution
    def speak(self):                                        # solution
        return "Miao!"                                      # solution
                                                            # solution
                                                            # solution
class Snake(Animal):                                        # solution
    def speak(self):                                        # solution
        return "Sssssss!"                                   # solution
