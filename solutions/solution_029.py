# RECALL RECALL RECALL RECALL RECALL RECALL RECALL RECALL RECALL
#
# THAT'S RIGHT! THIS IS A REPEAT FROM EARLIER! CAN YOU SOLVE
# IT WITHOUT LOOKING BACK?
#
# Complete the calculate_average function which accepts
# a list of numerical values and returns the average of
# the numbers.
#
# If the list of values is empty, the function should
# return None
#
# Do it without pseudocode, this time, from memory. Don't look
# at the last one you just wrote unless you really must.

def calculate_average(values):
    if len(values) == 0:                                # solution
        return None                                     # solution
    sum = 0                                             # solution
    for item in values:                                 # solution
        sum = sum + item                                # solution
    return sum / len(values)                            # solution
    # pass                                              # problem
