# Write a function that meets these requirements.
#
# Name:       generate_lottery_numbers
# Parameters: none
# Returns:    a list of six random unique numbers
#             between 1 and 40, inclusive
#
# Example bad results:
#    [4, 2, 3, 3, 1, 5] duplicate numbers
#    [1, 2, 3, 4, 5] not six numbers
#
# You can use randint from random, here, or any of
# the other applicable functions from the random
# package.
#
# https://docs.python.org/3/library/random.html

import random                                   # solution
                                                # noqa # solution
def generate_lottery_numbers():                 # noqa # solution
    numbers = []                                # solution
    while len(numbers) < 6:                     # solution
        number = random.randint(1, 40)          # solution
        if number not in numbers:               # solution
            numbers.append(number)              # solution
    return numbers                              # solution
                                                # noqa # solution
# or                                            # solution
                                                # noqa # solution
def generate_lottery_numbers():                 # noqa # solution
    numbers = list(range(1, 41))                # solution
    random.shuffle(numbers)                     # solution
    return numbers[0:6]                         # solution
