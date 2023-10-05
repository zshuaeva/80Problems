# Write a function that meets these requirements.
#
# Name:       safe_divide
# Parameters: two values, a numerator and a denominator
# Returns:    if the denominator is zero, then returns math.inf.
#             otherwise, returns numerator / denominator
#
# Don't for get to import math!

import math                                     # solution
                                                # noqa # solution
                                                # noqa # solution
def safe_divide(numerator, denominator):        # noqa # solution
    if denominator == 0:                        # solution
        return math.inf                         # solution
    return numerator / denominator              # solution
