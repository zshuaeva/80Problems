# Complete the gear_for_day function which returns a list of
# gear needed for the day given certain criteria.
#   * If the day is not sunny and it is a workday, the list
#     needs to contain "umbrella"
#   * If it is a workday, the list needs to contain "laptop"
#   * If it is not a workday, the list needs to contain
#     "surfboard"
#
# Do it without pseudocode, this time, from memory. Don't look
# at the last one you just wrote unless you really must.

def gear_for_day(is_workday, is_sunny):
    gear = []                                           # solution
    if is_workday and not is_sunny:                     # solution
        gear.append("umbrella")                         # solution
    if is_workday:                                      # solution
        gear.append("laptop")                           # solution
    else:                                               # solution
        gear.append("surfboard")                        # solution
    return gear                                         # solution
    # pass                                              # problem
