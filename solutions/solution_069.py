# Write a class that meets these requirements.
#
# Name:       Student
#
# Required state:
#    * name, a string
#
# Behavior:
#    * add_score(score)   # Adds a score to their list of scores
#    * get_average()      # Gets the average of the student's scores
#
# Example:
#    student = Student("Malik")
#
#    print(student.get_average())    # Prints None
#    student.add_score(80)
#    print(student.get_average())    # Prints 80
#    student.add_score(90)
#    student.add_score(82)
#    print(student.get_average())    # Prints 84
#
# There is pseudocode for you to guide you.


# class Student
class Student:                                              # solution
    # method initializer with required state "name"
    def __init__(self, name):                               # solution
        # self.name = name
        self.name = name                                    # solution
        # self.scores = [] because its an internal state
        self.scores = []                                    # solution

    # method add_score(self, score)
    def add_score(self, score):                             # solution
        # appends the score value to self.scores
        self.scores.append(score)                           # solution

    # method get_average(self)
    def get_average(self):                                  # solution
        # if there are no scores in self.scores
        if len(self.scores) == 0:                           # solution
            # return None
            return None                                     # solution
        # returns the sum of the scores divided by
        # the number of scores
        return sum(self.scores) / len(self.scores)          # solution
