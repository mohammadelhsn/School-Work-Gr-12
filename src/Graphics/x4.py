"""
1) How could you make a point move across the screen?  Create one moving from left to right at the same time as one is moving from top to bottom of the screen.

2) Have the CIRCLE/LINE that gets thicker as it move from left to right

2) Using recursion, create a spiral, like the one of the quiz, that continues to turn inward until it reaches the cente

3) Have a dot jump from one random location to another disappearing each time it jumps.
"""

from graphics import *
import time


def main():
    win = GraphWin("Moving Point", 200, 200)
    win.setBackground("yellow")
    win.setCoords(
        -(win.getWidth() / 2),
        -(win.getHeight() / 2),
        (win.getWidth() / 2),
        (win.getHeight() / 2),
    )

    # point1 = Point(0, -100)
    # point2 = Point(-100, 0)

    # for i in range(11):
    #     point1.draw(win)
    #     point2.draw(win)
    #     time.sleep(0.5)
    #     point1.move(0, 20)
    #     point2.move(20, 0)
    #     point1.undraw()
    #     point2.undraw()

    ln1 = Line(Point(-100, -100), Point(-100, 100))
    ln2 = Line(Point(-100, 100), Point(100, 100))

    ln1.draw(win)
    ln2.draw(win)

    win.getMouse()
    win.close()


main()
