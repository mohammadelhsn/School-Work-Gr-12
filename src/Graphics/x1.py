from graphics import *
from random import randint


def main():
    win = GraphWin("My point", 500, 500)
    win.setBackground("green")

    win.setCoords(
        -(win.getWidth() / 2),
        -(win.getHeight() / 2),
        (win.getWidth() / 2),
        (win.getHeight() / 2),
    )

    for i in range(20):
        point1 = Point(
            randint(-win.getWidth() / 2, win.getWidth() / 2),
            randint(-win.getHeight() / 2, win.getHeight() / 2),
        )
        point1.draw(win)

    win.getMouse()
    win.close()


main()
