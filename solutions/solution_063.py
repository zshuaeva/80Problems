# Write a function that meets these requirements.
#
# Name:       shift_letters
# Parameters: a string containing a single word
# Returns:    a new string with all letters replaced
#             by the next letter in the alphabet
#
# If the letter "Z" or "z" appear in the string, then
# they would get replaced by "A" or "a", respectively.
#
# Examples:
#     * inputs:  "import"
#       result:  "jnqpsu"
#     * inputs:  "ABBA"
#       result:  "BCCB"
#     * inputs:  "Kala"
#       result:  "Lbmb"
#     * inputs:  "zap"
#       result:  "abq"
#
# You may want to look at the built-in Python functions
# "ord" and "chr" for this problem

def shift_letters(word):                        # solution
    new_word = ""                               # solution
    for letter in word:                         # solution
        if letter == "Z":                       # solution
            new_letter = "A"                    # solution
        elif letter == "z":                     # solution
            new_letter = "a"                    # solution
        else:                                   # solution
            new_letter = chr(ord(letter) + 1)   # solution
        new_word += new_letter                  # solution
    return new_word                             # solution
