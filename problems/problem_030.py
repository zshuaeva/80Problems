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

# def find_second_largest(values):
#     if len(values) <= 1:
#         return None
#     new_list = sorted(values)
#     return new_list[len(new_list)-2]

def find_second_largest(values):
    if len(values) <= 1:                                # solution
        return None                                     # solution
    largest = [0]                                       # new variable
    second_largest = [0]                                # new variable assigned as first number / number at index[0]
    for current_value in values:                        # created variable called value to loop over values list
        if current_value > largest:                     # if current value is larger then largest
            second_largest = largest                    # make second_largest eqal to the value of largest
            largest = current_value                     # make largest equal to the CURRENT_value if larger than
        elif current_value > second_largest:            # if the current_value is largest than the second_largest
            second_largest = current_value              # assign second_largest to CURRENT_value
    return second_largest
