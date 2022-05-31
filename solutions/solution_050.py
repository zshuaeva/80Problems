# Write a function that meets these requirements.
#
# Name:       halve_the_list
# Parameters: a single list
# Returns:    two lists, each containing half of the original list
#             if the original list has an odd number of items, then
#             the extra item is in the first list
#
# Examples:
#    * input: [1, 2, 3, 4]
#      result: [1, 2], [3, 4]
#    * input: [1, 2, 3]
#      result: [1, 2], [3]

def halve_the_list(input):                              # solution
    return (                                            # solution
        input[0:len(input) // 2 + (len(input) % 2)],    # solution
        input[len(input) // 2 + (len(input) % 2):],     # solution
    )                                                   # solution
                                                        # noqa # solution
# or                                                    # solution
                                                        # noqa # solution
def halve_the_list(input):                              # noqa # solution
    first_list = []                                     # solution
    second_list = []                                    # solution
    first_list_len = len(input) // 2 + (len(input) % 2) # noqa # solution
    for i in range(first_list_len):                     # solution
        first_list.append(input[i])                     # solution
    for i in range(len(input) // 2):                    # solution
        index = i + first_list_len                      # solution
        second_list.append(input[index])                # solution
    return first_list, second_list                      # solution
