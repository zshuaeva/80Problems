# Complete the is_palindrome function to check if the value in
# the word parameter is the same backward and forward.
#
# For example, the word "racecar" is a palindrome because, if
# you write it backwards, it's the same word.
#
# Do it without pseudocode, this time, from memory. Don't look
# at the last one you just wrote unless you really must.

def is_palindrome(word):
    # Reverse the word into a list of letters
    # "hello" becomes ["o", "l", "l", "e", "h"]
    reversed_list_of_letters = reversed(word)

    # Join the letters together using the empty string
    # ["o", "l", "l", "e", "h"] becomes "olleh"
    reversed_word = "".join(reversed_list_of_letters)

    if reversed_word == word:                                   # solution
        return True                                             # solution
    else:                                                       # solution
        return False                                            # solution
    # pass                                                      # problem
