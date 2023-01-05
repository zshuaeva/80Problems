# Complete the calculate_sum function which accepts
# a list of numerical values and returns the sum of
# the numbers.
#
# If the list of values is empty, the function should
# return None
#

def calculate_sum(values):
    sum = 0
    if len(values) == 0:
        return None
        
    for i in values:
        sum += i
    return sum
