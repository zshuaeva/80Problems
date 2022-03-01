# Complete the reverse_dictionary function which has a
# single parameter that is a dictionary. Return a new
# dictionary that has the original dictionary's values
# for its keys, and the original dictionary's keys for
# its values.
#
# Examples:
#   * input:  {}
#     output: {}
#   * input:  {"key": "value"}
#     output: {"value", "key"}
#   * input:  {"one": 1, "two": 2, "three": 3}
#     output: {1: "one", 2: "two", 3: "three"}
#
# Do it without pseudocode, this time, from memory. Don't look
# at the last one you just wrote unless you really must.

def reverse_dictionary(dictionary):
    new_dictionary = {}                                 # solution
    for key, value in dictionary.items():               # solution
        new_dictionary[value] = key                     # solution
    return new_dictionary                               # solution
    # pass                                              # problem
