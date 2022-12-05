from graphics import *

def main():
    win = GraphWin("Assignment xx1", 500, 500)
    win.setBackground("grey")

    win.setCoords(
        -(win.getWidth() / 2),
        -(win.getHeight() / 2),
        (win.getWidth() / 2),
        (win.getHeight() / 2),
    )

    rect = Rectangle(Point(-90, -90), Point(90, 90))
    rect.setOutline("orange")
    rect.setFill("green")
    rect.setWidth(5)
    rect.draw(win)

    cir = Circle(Point(0, 0), 90)
    cir.setOutline("purple")
    cir.setWidth(5)
    cir.draw(win)

    label = Text(Point(0, 0), "circle / rect")
    label.setTextColor("black")
    label.setSize(10)
    label.draw(win)

    win.getMouse()
    win.close()
main()