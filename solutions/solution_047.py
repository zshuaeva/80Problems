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
    has_lowercase_letter = False                                        # solution
    has_uppercase_letter = False                                        # solution
    has_digit = False                                                   # solution
    has_special_char = False                                            # solution
    for character in password:                                          # solution
        if character.isalpha():                                         # solution
            if character.isupper():                                     # solution
                has_uppercase_letter = True                             # solution
            else:                                                       # solution
                has_lowercase_letter = True                             # solution
        elif character.isdigit():                                       # solution
            has_digit = True                                            # solution
        elif character == "$" or character == "!" or character == "@":  # solution
            has_special_char = True                                     # solution
    return (                                                            # solution
        len(password) >= 6                                              # solution
        and len(password) <= 12                                         # solution
        and has_lowercase_letter                                        # solution
        and has_uppercase_letter                                        # solution
        and has_digit                                                   # solution
        and has_special_char                                            # solution
    )                                                                   # solution
    # pass                                                              # problem
