# Write a function that meets these requirements.
#
# Name:       specific_random
# Parameters: none
# Returns:    a random number between 10 and 500, inclusive,
#             that is divisible by 5 and 7
#
# Examples:
#     * returns: 35
#     * returns: 105
#     * returns: 70
#
# Guidance:
#   * Generate all the numbers that are divisible by 5
#     and 7 into a list
#   * Use random.choice to select one

import random                               # solution
def specific_random():                      # noqa # solution
    good_numbers = []                       # solution
    for i in range(1, 500):                 # solution
        if i % 35 == 0:                     # solution
            good_numbers.append(i)          # solution
    return random.choice(good_numbers)      # solution
