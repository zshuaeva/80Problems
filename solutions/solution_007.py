# Complete the is_palindrome function to check if the value in
# the word parameter is the same backward and forward.
#
# For example, the word "racecar" is a palindrome because, if
# you write it backwards, it's the same word.
#
# There is pseudocode to guide you.

def is_palindrome(word):
    # Reverse the word into a list of letters
    # "hello" becomes ["o", "l", "l", "e", "h"]
    reversed_list_of_letters = reversed(word)

    # Join the letters together using the empty string
    # ["o", "l", "l", "e", "h"] becomes "olleh"
    reversed_word = "".join(reversed_list_of_letters)

    # If reversed_word equals word
    if reversed_word == word:                                   # solution
        # return True
        return True                                             # solution
    # Otherwise
    else:                                                       # solution
        # return False
        return False                                            # solution
    # pass                                                      # problem
