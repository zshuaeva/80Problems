# Write a function that meets these requirements.
#
# Name:       sum_fraction_sequence
# Parameters: a number
# Returns:    the sum of the fractions of the
#             form 1/2+2/3+3/4+...+number/number+1
#
# Examples:
#     * input:   1
#       returns: 1/2
#     * input:   2
#       returns: 1/2 + 2/3
#     * input:   3
#       returns: 1/2 + 2/3 + 3/4

def sum_fraction_sequence(num):
    result = 0
    for i in range(num + 1):
        print(i)
        result += (i/(i+1))
    return result

print(sum_fraction_sequence(6))
