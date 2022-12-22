from graphics import *

win = GraphWin("Boxes and Ovals", 200, 200)
win.setBackground("grey")
win.setCoords(0.0, 0.0, 3.0, 3.0)
Line(Point(1, 0), Point(1, 3)).draw(win)
Line(Point(2, 0), Point(2, 3)).draw(win)
Line(Point(0, 1), Point(3, 1)).draw(win)
Line(Point(0, 2), Point(3, 2)).draw(win)
turn = 0


def draw(*points: Point):
    global turn
    if turn == 0:
        Oval(points[0], points[1]).draw(win).setFill("green")
        turn = 1
    else:
        Rectangle(points[2], points[3]).draw(win).setFill("red")
        turn = 0


def current():
    if turn == 0:
        return "Oval"
    else:
        return "Square"


class Board:
    def __init__(self):
        self.top = {"left": "", "middle": "", "right": ""}
        self.middle = {"left": "", "middle": "", "right": ""}
        self.bottom = {"left": "", "middle": "", "right": ""}

    def update(self, row, column, new):
        if row == "top":
            self.top[column] = new
            self.top = self.top 
        if row == "middle":
            self.middle[column] = new
            self.middle = self.middle
        if row == "bottom":
            self.bottom[column] = new
            print(self.bottom[column])
            self.bottom = self.bottom
            print(self.bottom)


for i in range(9):
    p = win.getMouse()
    b = Board()

    print(f"Top {b.top}")
    print(f"Middle {b.middle}")
    print(f"Bottom {b.bottom}")

    if p.getX() < 1:
        if p.getY() < 1:  # column1, row1
            draw(Point(0, 0), Point(1, 1), Point(0.1, 0.1), Point(0.9, 0.9))
            b.update("bottom", "left", current())
        if p.getY() < 2 and p.getY() > 1:
            draw(Point(0, 1), Point(1, 2), Point(0.1, 1.1), Point(0.9, 1.9))
            b.update("middle", "left", current())
        if p.getY() < 3 and p.getY() > 2:
            draw(Point(0, 2), Point(1, 3), Point(0.1, 2.1), Point(0.9, 2.9))
            b.update("top", "left", current())
    if p.getX() < 2 and p.getX() > 1:
        if p.getY() < 1:
            draw(Point(1, 0), Point(2, 1), Point(1.1, 0.1), Point(1.9, 0.9))
            b.update("bottom", "middle", current())
        if p.getY() < 2 and p.getY() > 1:
            draw(Point(1, 1), Point(2, 2), Point(1.1, 1.1), Point(1.9, 1.9))
            b.update("middle", "middle", current())
        if p.getY() < 3 and p.getY() > 2:
            draw(Point(1, 2), Point(2, 3), Point(1.1, 2.1), Point(1.9, 2.9))
            b.update("top", "middle", current())
    if (p.getX() < 3) and p.getX() > 2:
        if p.getY() < 1:
            draw(Point(2, 0), Point(3, 1), Point(2.1, 0.1), Point(2.9, 0.9))
            b.update("bottom", "right", current())
        if p.getY() < 2 and p.getY() > 1:
            draw(Point(2, 1), Point(3, 2), Point(2.1, 1.1), Point(2.9, 1.9))
            b.update("middle", "right", current())
        if p.getY() < 3 and p.getY() > 2:
            draw(Point(2, 2), Point(3, 3), Point(2.1, 2.1), Point(2.9, 2.9))
            b.update("top", "right", current())

win.getMouse()
win.close()
