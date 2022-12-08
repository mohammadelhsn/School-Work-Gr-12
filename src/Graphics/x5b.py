from graphics import *
from random import randint

def main():
    win = GraphWin("Where's Waldo", 200, 200)

    win.setCoords(
        -(win.getWidth() / 2),
        -(win.getHeight() / 2),
        (win.getWidth() / 2),
        (win.getHeight() / 2),
    )

    p1 = -randint(-50, 0)
    p2 = -randint(-50, 0)

    rect = Rectangle(Point(p1, p2), Point(p1 + 20, p2 + 20))
    rect.draw(win)

    P1: Point = rect.getP1()
    P2: Point = rect.getP2()

    

    P1.setFill("orange")
    P1.draw(win)
    P2.setFill("green")
    P2.draw(win)

    for i in range(5):
        p = win.getMouse()
        pt = Point(p.getX(), p.getY())

        if pt.getX() >= P1.getX() and pt.getX() <= P2.getX():
            if pt.getY() >= P1.getY() and pt.getY() <= P2.getY():
                print("You've found Waldo!")
                break
            else:
                print("It's not in the box")
                continue
        else:
            print("It's not in the box")
            continue

    win.getMouse()
    win.close()


main()
