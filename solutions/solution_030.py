# Complete the find_second_largest function which accepts
# a list of numerical values and returns the second largest
# in the list
#
# If the list of values is empty, the function should
# return None
#
# If the list of values has only one value, the function
# should return None
#
# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def find_second_largest(values):
    if len(values) <= 1:                                # solution
        return None                                     # solution
    largest = values[0]                                 # solution
    second_largest = values[0]                          # solution
    for value in values:                                # solution
        if value > largest:                             # solution
            second_largest = largest                    # solution
            largest = value                             # solution
        elif value > second_largest:                    # solution
            second_largest = value                      # solution
    return second_largest                               # solution
    # pass                                              # problem
