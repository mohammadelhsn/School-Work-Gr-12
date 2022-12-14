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

    line1 = Line(Point(100, 90), Point(-100, 90))
    line2 = Line(Point(-100, 90), Point(-100, -100))
    line3 = Line(Point(-100, -100), Point(100, -100))
    line4 = Line(Point(100, -100), Point(100, 100))

    change = 10

    def draw_spiral(l1, l2, l3, l4):
        if l1.p1.x == 0:
            return
        else:
            l1.draw(win)
            l2.draw(win)
            l3.draw(win)
            l4.draw(win)
            li1 = Line(
                Point(l1.getP1().x - change, l1.getP1().y - change),
                Point(l1.getP2().x + change, l1.getP2().y - change),
            )
            li2 = Line(
                Point(l2.p1.x + change, l2.p1.y - change),
                Point(l2.p2.x + change, l2.p2.y + change),
            )
            li3 = Line(
                Point(l3.p1.x + change, l3.p1.y + change),
                Point(l3.p2.x - change, l3.p2.y + change),
            )
            li4 = Line(
                Point(l4.p1.x - change, l4.p1.y + change),
                Point(l4.p2.x - change, l4.p2.y - change),
            )
        return draw_spiral(li1, li2, li3, li4)

    draw_spiral(line1, line2, line3, line4)
    win.getMouse()
    win.close()


main()
