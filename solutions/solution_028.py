# Complete the remove_duplicate_letters that takes a string
# parameter "s" and returns a string with all of the
# duplicates removed.
#
# Examples:
#   * For "abc", the result is "abc"
#   * For "abcabc", the result is "abc"
#   * For "abccba", the result is "abc"
#   * For "abccbad", the result is "abcd"
#
# If the list is empty, then return the empty string.
#
# There is some pseudocode to guide you.

def remove_duplicate_letters(s):
    # result = new empty string
    result = ""                                         # solution
    # for every letter in the string s
    for letter in s:                                    # solution
        # if the letter is not in the result
        if letter not in result:                        # solution
            # add it to the end of the result
            result = result + letter                    # solution
    # return the result
    return result                                       # solution
    # pass                                              # problem
