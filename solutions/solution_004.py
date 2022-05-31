# Complete the max_of_three function so that returns the
# maximum of three values.
#
# If two values are the same maximum value, return either of
# them.
# If the all of the values are the same, return any of them
#
# Use the >= operator for greater than or equal to
#
# Do it without pseudocode, this time, from memory. Don't look
# at the last one you just wrote unless you really must.

def max_of_three(value1, value2, value3):
    if value1 >= value2 and value1 >= value3:                   # solution
        return value1                                           # solution
    elif value2 >= value1 and value2 >= value3:                 # solution
        return value2                                           # solution
    else:                                                       # solution
        return value3                                           # solution
    # pass                                                      # problem
