# Complete the check_password function that accepts a
# single parameter, the password to check.
#
# A password is valid if it meets all of these criteria
#   * It must have at least one lowercase letter (a-z)
#   * It must have at least one uppercase letter (A-Z)
#   * It must have at least one digit (0-9)
#   * It must have at least one special character $, !, or @
#   * It must have six or more characters in it
#   * It must have twelve or fewer characters in it
#
# The string object has some methods that you may want to use,
# like ".isalpha", ".isdigit", ".isupper", and ".islower"

def check_password(password):
# check for one lowercase
# check for one uppercase
# check for one digit
# check for $, !, or @
# check if >= 6 or <= 12
# return if all are true
    if_lower = False
    if_upper = False
    if_digit = False
    if_char = False
    if_len = False

    for i in password:
        if i.islower() == True:
            if_lower == True
        if i.isupper() == True:
            if_upper == True
        if i.isdigit() == True:
            if_digit == True
        if i == "$" or i == "!" or i == "@":
            if_char == True
        if len(password) >= 6 and len(password) <= 12 == True:
            if_len == True
    return (if_lower and if_upper and if_digit and if_char and if_len)
