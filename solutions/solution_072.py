# Write a class that meets these requirements.
#
# Name:       Person
#
# Required state:
#    * name, a string
#    * hated foods list, a list of names of food they don't like
#    * loved foods list, a list of names of food they really do like
#
# Behavior:
#    * taste(food name)  * returns None if the food name is not in their
#                                  hated or loved food lists
#                        * returns True if the food name is in their
#                                  loved food list
#                        * returns False if the food name is in their
#                                  hated food list
#
# Example:
#    person = Person("Malik",
#                    ["cottage cheese", "sauerkraut"],
#                    ["pizza", "schnitzel"])
#
#    print(person.taste("lasagna"))     # Prints None, not in either list
#    print(person.taste("sauerkraut"))  # Prints False, in the hated list
#    print(person.taste("pizza"))       # Prints True, in the loved list
#
# Do it without pseudocode, this time, from memory. Don't look
# at the last one you just wrote unless you really must.


class Person:                                                       # solution
    def __init__(self, name, hated_foods, loved_foods):             # solution
        self.name = name                                            # solution
        self.hated_foods = hated_foods                              # solution
        self.loved_foods = loved_foods                              # solution
                                                                    # noqa # solution
    def taste(self, food):                                          # noqa # solution
        if food in self.hated_foods:                                # solution
            return False                                            # solution
        elif food in self.loved_foods:                              # solution
            return True                                             # solution
        else:                                                       # solution
            return None                                             # solution
