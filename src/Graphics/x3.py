"""
MINI-ASSIGNMENT x3:

Use the input to display choices of the following menu in a while loop : A ) circle (use the input for dimensions, outline and colour) B) a rectangle (use the input for dimensions, outline and colour) 

C) text (print out on the screen what the person inputs including font/bold/italic etc)

D) to exit

"""

from graphics import *


def main():
    win = GraphWin("Mini-Assignment x3", 500, 500)
    win.setBackground("grey")

    win.setCoords(
        -(win.getWidth() / 2),
        -(win.getHeight() / 2),
        (win.getWidth() / 2),
        (win.getHeight() / 2),
    )

    action = int(
        input(
            "What would you like to do?\n1) A circle\n2) Rectangle\n3) Text\n4) Quit "
        )
    )

    if action == 1:
        dimensions = int(input("What are the dimensions for the circle? "))
        outline = input(
            'If you would like the outline, enter the name of the colour, if not, enter "no" '
        )

        cir = Circle(Point(0, 0), dimensions)

        if outline != "no":
            cir.setOutline(outline)

        cir.draw(win)

    if action == 2:
        dimensions = int(input("What are the dimensions for the circle? "))
        outline = input(
            'If you would like the outline, enter the name of the coloutr, if not, enter "no" '
        )

        rect = Rectangle(Point(-dimensions, -dimensions), Point(dimensions, dimensions))

        if outline != "no":
            rect.setOutline(outline)

        rect.draw(win)

    if action == 3:
        text = input("What would you like to write to the screen? ")
        font = input("What font would you like to use? ")
        styling = input("What style would you like on the font? (bold/italic/none) ")

        if styling == "none":
            styling = "normal"

        label = Text(Point(0, 0), text)
        label.setFace(font)
        label.setStyle(styling)
        label.draw(win)

    if action == 4:
        return

    win.getMouse()
    win.close()


main()
