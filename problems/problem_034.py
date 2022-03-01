# Complete the count_letters_and_digits function which
# accepts a parameter s that contains a string and returns
# two values, the number of letters in the string and the
# number of digits in the string
#
# Examples:
#   * "" returns 0, 0
#   * "a" returns 1, 0
#   * "1" returns 0, 1
#   * "1a" returns 1, 1
#
# To test if a character c is a digit, you can use the
# c.isdigit() method to return True of False
#
# To test if a character c is a letter, you can use the
# c.isalpha() method to return True of False
#
# Remember that functions can return more than one value
# in Python. You just use a comma with the return, like
# this:
#      return value1, value2
#
# This problem has pseudocode to guide you.

def count_letters_and_digits(s):
    # number of letters = 0
    # number of digits = 0
    # for each character c in s
        # if the character c is a digit (c.isdigit())
            # add one to the number of digits
        # if the character c is a letter (c.isalpha())
            # add one to the number of letters
    # return number of letters, number of digits
    pass
