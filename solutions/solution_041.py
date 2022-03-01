# Complete the add_csv_lines function which accepts a list
# as its only parameter. Each item in the list is a
# comma-separated string of numbers. The function should
# return a new list with each entry being the corresponding
# sum of the numbers in the comma-separated string.
#
# These kinds of strings are called CSV strings, or comma-
# sepearted values strings.
#
# Examples:
#   * input:  []
#     output: []
#   * input:  ["3", "1,9"]
#     output: [3, 10]
#   * input:  ["8,1,7", "10,10,10", "1,2,3"]
#     output:  [16, 30, 6]
#
# Look up the string split function to find out how to
# split a string into pieces.
#
# Do it without pseudocode, this time, from memory. Don't look
# at the last one you just wrote unless you really must.
#
# Write out your own pseudocode to help guide you.

def add_csv_lines(csv_lines):
    result_list = []                                    # solution
    for item in csv_lines:                              # solution
        pieces = item.split(",")                        # solution
        line_sum = 0                                    # solution
        for piece in pieces:                            # solution
            value = int(piece)                          # solution
            line_sum += value                           # solution
        result_list.append(line_sum)                    # solution
    return result_list                                  # solution
    # pass                                              # problem
