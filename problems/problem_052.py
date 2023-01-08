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
    # generate number between 1, 40
        #add to number list
    #failed -- saying numbers not unique, must check values in number list
    #return number list

import random
def generate_lottery_numbers():
    number_list = []
    while len(number_list) < 6:
        selection = random.randint(1, 40)
        if selection not in number_list:
            number_list.append(selection)
    return number_list
print(generate_lottery_numbers())
