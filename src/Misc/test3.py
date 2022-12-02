from graphics import *


def main():
    win = GraphWin("My mouse clicks", 200, 200)
    win.setBackground("grey")
    for i in range(10):
        p = win.getMouse()
        x = p.getX()
        y = p.getY()
        point1 = Point(x, y)
        point1.draw(win)
        print(f"You clicked at: ({x} ,{y})")


main()
