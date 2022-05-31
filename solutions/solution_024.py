# Complete the calculate_average function which accepts
# a list of numerical values and returns the average of
# the numbers.
#
# If the list of values is empty, the function should
# return None
#
# Pseudocode is available for you

def calculate_average(values):
    # If there are no items in the list of values
    if len(values) == 0:                                # solution
        # return None
        return None                                     # solution
    # sum = 0
    sum = 0                                             # solution
    # for each item in the list of values
    for item in values:                                 # solution
        # add it to the sum
        sum = sum + item                                # solution
    # return the sum divided by the number of items
    # in the list
    return sum / len(values)                            # solution
    # pass                                              # problem
