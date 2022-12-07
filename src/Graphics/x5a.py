from graphics import *


def main():
    win = GraphWin("Mini-Assignment x5a", 500, 500)
    win.setBackground("grey")

    win.setCoords(
        -(win.getWidth() / 2),
        -(win.getHeight() / 2),
        (win.getWidth() / 2),
        (win.getHeight() / 2),
    )

    shape = int(
        input(
            "What would you like to draw?\n1) A triangle\n2) Rectangle\n3) 5-sided shape "
        )
    )
    
    pt_count = shape + 2

    verticies = []
    for i in range(pt_count):
        p1 = win.getMouse()
        p1.draw(win)
        verticies.append(p1)

    shape = Polygon(verticies)
    shape.draw(win)

    win.getMouse()
    win.close()


main()
