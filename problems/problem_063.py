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

def shift_letters(str):
    new_str = ""
    for i in str:
        if i == "Z":
            replace = "A"
        elif i == "z":
            replace = "a"
        else:
            replace = chr(ord(i) + 1)
        new_str += replace
    return new_str


print(shift_letters("Zahara"))
