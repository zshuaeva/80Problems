# Complete the has_quorum function to test to see if the number
# of the people in the attendees list is greater than or equal
# to 50% of the number of people in the members list.

def has_quorum(attendees_list, members_list):
    half = len(members_list) / 2
    if len(attendees_list) >= half:
        return True
    else:
        return False
