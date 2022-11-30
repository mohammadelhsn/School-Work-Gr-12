from graphics import *
from random import randint


def main():
    win = GraphWin("My point", 200, 200)
    win.setBackground("green")

    for i in range(20):
        point1 = Point(randint(-100, 100), randint(-100, 100))
        point1.draw(win)

    win.getMouse()
    win.close()


main()
