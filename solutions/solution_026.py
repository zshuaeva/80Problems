# Complete the calculate_grade function which accepts
# a list of numerical scores each between 0 and 100.
#
# Based on the average of the scores, the function
# returns
#   * An "A" for an average greater than or equal to 90
#   * A "B" for an average greater than or equal to 80
#     and less than 90
#   * A "C" for an average greater than or equal to 70
#     and less than 80
#   * A "D" for an average greater than or equal to 60
#     and less than 70
#   * An "F" for any other average

def calculate_grade(values):
    if len(values) == 0:                                # solution
        return None                                     # solution
    sum = 0                                             # solution
    for item in values:                                 # solution
        sum = sum + item                                # solution
    average = sum / len(values)                         # solution
    if average >= 90:                                   # solution
        return "A"                                      # solution
    elif average >= 80:                                 # solution
        return "B"                                      # solution
    elif average >= 70:                                 # solution
        return "C"                                      # solution
    elif average >= 60:                                 # solution
        return "D"                                      # solution
    else:                                               # solution
        return "F"                                      # solution
    # pass                                              # problem
