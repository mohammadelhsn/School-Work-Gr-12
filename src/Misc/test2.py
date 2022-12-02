from graphics import *

win = GraphWin("agar.io", 800, 800)
win.setBackground("yellow")


class Agario:
    def __init__(self, size, name, colour, x, y) -> None:
        self.radius = size
        self.colour = colour
        self.name = name
        self.x = x
        self.y = y

    def circle(self):
        circ1 = Circle(Point(self.x, self.y), self.radius)
        circ1.setFill(self.colour)
        self.circ1 = circ1

    def text(self):
        label = Text(Point(self.x, self.y), self.name)
        label.setFill("white")
        self.label = label

    def draw(self):
        self.circ1.draw(win)
        self.label.draw(win)


player1 = Agario(50, "Mohammad", "green", 300, 250)

player1.circle()
player1.text()
player1.draw()

win.getMouse()
win.close()
