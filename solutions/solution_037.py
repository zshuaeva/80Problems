# Complete the pad_left function which takes three parameters
#   * a number
#   * the number of characters in the result
#   * a padding character
# and turns the number into a string of the desired length
# by adding the padding character to the left of it
#
# Examples:
#   * number: 10
#     length: 4
#     pad:    "*"
#     result: "**10"
#   * number: 10
#     length: 5
#     pad:    "0"
#     result: "00010"
#   * number: 1000
#     length: 3
#     pad:    "0"
#     result: "1000"
#   * number: 19
#     length: 5
#     pad:    " "
#     result: "   19"
#
# Do it without pseudocode, this time, from memory. Don't look
# at the last one you just wrote unless you really must.

def pad_left(number, length, pad):
    s = str(number)                                     # solution
    while len(s) < length:                              # solution
        s = pad + s                                     # solution
    return s                                            # solution
    # pass                                              # problem
