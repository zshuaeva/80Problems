# Complete the gear_for_day function which returns a list of
# gear needed for the day given certain criteria.
#   * If the day is not sunny and it is a workday, the list
#     needs to contain "umbrella"
#   * If it is a workday, the list needs to contain "laptop"
#   * If it is not a workday, the list needs to contain
#     "surfboard"
#
# There is pseudocode to guide you.

def gear_for_day(is_workday, is_sunny):
    # Create an empty list that will hold the different gear
    # gear = new empty list
    gear = []
    # If it is a workday and it is not sunny
    if is_workday and not is_sunny:                     # solution
        # Add "umbrella" to gear
        # gear.append("umbrella")
        gear.append("umbrella")                         # solution
    # If it is a workday
    if is_workday:                                      # solution
        # Add "laptop" to gear
        gear.append("laptop")                           # solution
    # Otherwise
    else:                                               # solution
        # Add "surfboard" to gear
        gear.append("surfboard")                        # solution
    # Return the list of gear
    return gear                                         # solution
