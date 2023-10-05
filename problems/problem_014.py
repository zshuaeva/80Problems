# Complete the can_make_pasta function to
# * Return true if the ingredients list contains
#   "flour", "eggs", and "oil"
# * Otherwise, return false
#
# The ingredients list will always contain three items.

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def can_make_pasta(ingredients):
#    #create list check variable
    # iterate over ingredient list
        #if current ingredient == "flour"
            #list check += 1
        #if current ingredient == "eggs"
            #list check += 1
        #if current_ingredient == "oil"
            #list_check += 1#
    check_list = 0
    for i in ingredients:
        if i == "flour":
            check_list += 1
        if i == "eggs":
            check_list += 1
        if i == "oil":
            check_list += 1
    if check_list == 3:
        return True
    return False
