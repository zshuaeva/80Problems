# Write a function that meets these requirements.
#
# Name:       halve_the_list
# Parameters: a single list
# Returns:    two lists, each containing half of the original list
#             if the original list has an odd number of items, then
#             the extra item is in the first list
#
# Examples:
#    * input: [1, 2, 3, 4]
#      result: [1, 2], [3, 4]
#    * input: [1, 2, 3]
#      result: [1, 2], [3]

def halve_the_list(list):
    #i: single list
    #o: two list, containing half of input list- if list is odd, first list should have extra item
    #create two result variables
        #get length of list / 2
    # if list is %3, use ceiling for first half
    #create condition to append first half, second half
    first_half = []
    second_half = []
    first_len = 0
    second_len = 0
    if len(list) % 2 == 1:
        first_len = (len(list) // 2) + 1
        second_len = len(list) // 2
    else:
        first_len = len(list) // 2
        second_len = len(list) // 2
    print(first_len)
    print(second_len)

    for i in range(first_len):
        first_half.append(list[i])
    for k in range(second_len):
        index = k + first_len
        second_half.append(list[index])
    return first_half, second_half
print(halve_the_list([1, 2, 3, 4, 5, 6]))
