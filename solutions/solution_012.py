# Complete the fizzbuzz function to return
# * The word "fizzbuzz" if number is evenly divisible by
#   by both 3 and 5
# * The word "fizz" if number is evenly divisible by only
#   3
# * The word "buzz" if number is evenly divisible by only
#   5
# * The number if it is not evenly divisible by 3 nor 5
#
# Try to combine what you have done in the last two problems
# from memory.

def fizzbuzz(number):
    if number % 5 == 0 and number % 3 == 0:             # solution
        return "fizzbuzz"                               # solution
    elif number % 3 == 0:                               # solution
        return "fizz"                                   # solution
    elif number % 5 == 0:                               # solution
        return "buzz"                                   # solution
    else:                                               # solution
        return number                                   # solution
    # pass                                              # problem
