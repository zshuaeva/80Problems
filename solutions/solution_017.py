# Complete the is_inside_bounds function which has the
# following parameters:
#   x: the x coordinate to check
#   y: the y coordinate to check
#   rect_x: The left of a rectangle
#   rect_y: The top of a rectangle
#   rect_width: The width of the rectangle
#   rect_height: The height of the rectangle
#
# The is_inside_bounds function returns true if all of
# the following are true
#   * x is greater than or equal to rect_x
#   * y is greater than or equal to rect_y
#   * x is less than or equal to rect_x + rect_width
#   * y is less than or equal to rect_y + rect_height
#
# There is pseudo code to guide you.

def is_inside_bounds(x, y, rect_x, rect_y, rect_width, rect_height):
    # If x is greater than or equal to rect_x
    # and y is greater than or equal to rect_y
    # and x is less than or equal to rect_x + rect_width
    # and y is less than or equal to rect_y + rect_height
    if (                                                # solution
        x >= rect_x                                     # solution
        and y >= rect_y                                 # solution
        and x <= rect_x + rect_width                    # solution
        and y <= rect_y + rect_height                   # solution
    ):                                                  # solution
        # return True
        return True                                     # solution
    # Otherwise
    else:                                               # solution
        # return False
        return False                                    # solution
    # pass                                              # problem
