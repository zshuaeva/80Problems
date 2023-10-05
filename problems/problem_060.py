# Write a function that meets these requirements.
#
# Name:       only_odds
# Parameters: a list of numbers
# Returns:    a copy of the list that only includes the
#             odd numbers from the original list
#
# Examples:
#     * input:   [1, 2, 3, 4]
#       returns: [1, 3]
#     * input:   [2, 4, 6, 8]
#       returns: []
#     * input:   [1, 3, 5, 7]
#       returns: [1, 3, 5, 7]

def only_odd(num_list):
    if len(num_list) == 0:
        return None
    filtered_list = []
    for i in num_list:
        if i % 2 != 0:
            filtered_list.append(i)
    return filtered_list

print(only_odd([2, 4, 6, 8]))
