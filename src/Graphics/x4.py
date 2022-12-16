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

    point1 = Point(0, -100)
    point2 = Point(-100, 0)

    for i in range(11):
        point1.draw(win)
        point2.draw(win)
        time.sleep(0.5)
        point1.move(0, 20)
        point2.move(20, 0)
        point1.undraw()
        point2.undraw()

    # draw a circle on the left and as it goes to the right, it's size increases

    circle = Circle(Point(-90, -90), 10)

    circle.draw(win)

    for i in range(18):
        time.sleep(1)
        circle.undraw()
        circle.p2.x += 10
        circle.p2.y += 10
        circle.radius += 5
        circle.draw(win)

    circle.undraw()

    line1 = Line(Point(100, 90), Point(-100, 90))
    line2 = Line(Point(-100, 90), Point(-100, -100))
    line3 = Line(Point(-100, -100), Point(100, -100))
    line4 = Line(Point(100, -100), Point(100, 100))

    change = 10
    lines = []
    lines.append(line1)
    lines.append(line2)
    lines.append(line3)
    lines.append(line4)

    def draw_spiral(l1, l2, l3, l4):
        if l1.p1.x == 0:
            return
        else:
            l1.draw(win)
            l2.draw(win)
            l3.draw(win)
            l4.draw(win)
            li1 = Line(
                Point(l1.p1.x - change, l1.p1.y - change),
                Point(l1.p2.x + change, l1.p2.y - change),
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
            lines.append(l1)
            lines.append(l2)
            lines.append(l3)
            lines.append(l4)
        return draw_spiral(li1, li2, li3, li4)

    draw_spiral(line1, line2, line3, line4)

    time.sleep(5)

    for line in lines:
        line.undraw()

    win.getMouse()
    win.close()


main()
