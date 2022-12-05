from graphics import *


def main():
    win = GraphWin("Initials", 500, 500)
    win.setBackground("green")

    win.setCoords(
        -(win.getWidth() / 2),
        -(win.getHeight() / 2),
        (win.getWidth() / 2),
        (win.getHeight() / 2),
    )

    point1 = Point(30, 30)
    point2 = Point(30, 60)
    point3 = Point(45, 30)
    point4 = Point(60, 60)
    point5 = Point(60, 30)
    point6 = Point(80, 30)
    point7 = Point(80, 60)
    point8 = Point(100, 30)
    point9 = Point(100, 45)
    point10 = Point(100, 60)

    line = Line(point1, point2)
    line2 = Line(point2, point3)
    line3 = Line(point3, point4)
    line4 = Line(point4, point5)
    line5 = Line(point6, point7)
    line6 = Line(point6, point8)
    line7 = Line(Point(80, 45), point9)
    line8 = Line(point7, point10)

    line.setWidth(4)
    line.draw(win)
    line2.setWidth(4)
    line2.draw(win)
    line3.setWidth(4)
    line3.draw(win)
    line4.setWidth(4)
    line4.draw(win)
    line5.setWidth(4)
    line5.draw(win)
    line6.setWidth(4)
    line7.setWidth(4)
    line8.setWidth(4)
    line6.draw(win)
    line7.draw(win)
    line8.draw(win)

    win.getMouse()
    win.close()


main()
