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
# Do it without pseudocode, this time, from memory. Don't look
# at the last one you just wrote unless you really must.


class Student:                                              # solution
    def __init__(self, name):                               # solution
        self.name = name                                    # solution
        self.scores = []                                    # solution

    def add_score(self, score):                             # solution
        self.scores.append(score)                           # solution

    def get_average(self):                                  # solution
        if len(self.scores) == 0:                           # solution
            return None                                     # solution
        return sum(self.scores) / len(self.scores)          # solution
