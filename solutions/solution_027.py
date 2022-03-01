# Complete the max_in_list function to find the
# maximum value in a list
#
# If the list is empty, then return None.
#
# There is some pseudocode to guide you.

def max_in_list(values):
    # if there are no items in the values list
    if len(values) == 0:                                # solution
        # return None
        return None                                     # solution
    # max value = first item in the values list
    max_value = values[0]                               # solution
    # for each item in the values list
    for item in values:                                 # solution
        # if item is greater than the max value
        if item > max_value:                            # solution
            # max value = item
            max_value = item                            # solution
    # return the max value
    return max_value                                    # solution
    # pass                                              # problem
