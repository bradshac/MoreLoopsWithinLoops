"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of TWO-DIMENSIONAL GRAPHICS.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Alexander Bradshaw.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to test them. """
    run_test_draw_upside_down_wall()


def run_test_draw_upside_down_wall():
    """ Tests the    draw_upside_down_wall    function. """
    # Tests 1 and 2 are ALREADY DONE (here).
    window = rg.RoseWindow(550, 300, 'Upside-down wall, Tests 1 and 2')

    rectangle = rg.Rectangle(rg.Point(125, 230), rg.Point(155, 250))
    draw_upside_down_wall(rectangle, 8, window)

    rectangle = rg.Rectangle(rg.Point(375, 175), rg.Point(425, 225))
    draw_upside_down_wall(rectangle, 4, window)

    window.close_on_mouse_click()


def draw_upside_down_wall(rectangle, n, window):
    """
    See   MoreWalls.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an "upside-down wall" on the given window, where:
      -- The BOTTOM of the wall is a single "brick"
            that is the given rg.Rectangle.
      -- There are n rows in the wall.
      -- Each row is a row of "bricks" that are the same size
            as the given rg.Rectangle.
      -- Each row has one more brick than the row below it.
      -- Each row is centered on the bottom row.

    Preconditions:
      :type rectangle: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
    and n is nonnegative.
    """
    # ------------------------------------------------------------------
    # Done: 2. Implement and test this function.
    #     Some tests are already written for you (above).
    # ------------------------------------------------------------------
    x2 = rectangle.corner_2.x
    x1 = rectangle.corner_1.x
    y1 = rectangle.corner_1.y
    y2 = rectangle.corner_2.y
    org_x1 = x1
    org_x2 = x2
    half_length = abs(rectangle.corner_1.x-rectangle.corner_2.x)/2
    length = abs(rectangle.corner_1.x-rectangle.corner_2.x)
    width = abs(rectangle.corner_2.y - rectangle.corner_1.y)
    print(y1)
    for k in range(n):
        for j in range(k+1):
            new_rectangle = rg.Rectangle(rg.Point(x1, y1), rg.Point(x2, y2))
            new_rectangle.attach_to(window)
            window.render(.01)
            x1 += length
            x2 += length
        x1 = org_x1
        x2 = org_x2
        x1 = x1 - (k+1)*half_length
        x2 = x2 - (k+1) * half_length
        y1 = y1 - width
        y2 = y2 - width





# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
