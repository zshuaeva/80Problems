# Complete the is_palindrome function to check if the value in
# the word parameter is the same backward and forward.
#
# For example, the word "racecar" is a palindrome because, if
# you write it backwards, it's the same word.

# It uses the built-in function reversed and the join method
# for string objects.

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.


def is_palindrome(word):
    letterList = []
    reversedList = []
    for letters in word:
        letterList.append(letters)
        reversedList.append(letters)
    reversedList.reverse()

    if letterList == reversedList:
        return True
    else:
        return False


print(is_palindrome("WOW"), "<--- should return TRUE")
print(is_palindrome("car"), "<--- should return FALSE")
