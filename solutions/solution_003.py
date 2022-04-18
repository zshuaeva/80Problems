# Complete the max_of_three function so that returns the
# maximum of three values.
#
# If two values are the same maximum value, return either of
# them. If all of the values are the same, return any of
# them
#
# Use the >= operator for greater than or equal to
#
# Pseudocode is provided for you to guide you along the way.

def max_of_three(value1, value2, value3):
    # If value1 is greater than or equal to value2
    # and value1 is greater than or equal to value3
    if value1 >= value2 and value1 >= value3:                   # solution
        # Return value1
        return value1                                           # solution
    # Otherwise, if value2 is greater than or equal to value1
    # and value2 is greater than or equal to value3
    elif value2 >= value1 and value2 >= value3:                 # solution
        # Return value2
        return value2                                           # solution
    # Otherwise,
    else:                                                       # solution
        # Return value3
        return value3                                           # solution
    # pass                                                      # problem
