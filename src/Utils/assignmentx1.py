from graphics import *

win = GraphWin("Assignment xx1", 500, 500)
win.setBackground("grey")

win.setCoords(
    -(win.getWidth() / 2),
    -(win.getHeight() / 2),
    (win.getWidth() / 2),
    (win.getHeight() / 2),
)


cir = Circle(Point(0, 0), 90)
cir.draw(win)


win.getMouse()
win.close()
