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

def pad_left(number, length, pad):
    #I: number to be printed, total length of string, and the padding character
    #O: padded character*length(-input#length) + input number,
    #create empty string
    #iterate by range of length minus input number
    #return emptystring + input number or pass into as str(number)

    result = ""
    for i in range(length - len(str(number))):
        print(i)
        result += pad
    return result + str(number)

# print(pad_left(10, 4, "*"))
