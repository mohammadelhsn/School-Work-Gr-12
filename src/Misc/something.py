import turtle


class Button:
    colour: str
    size: int
    text: str

    def __init__(self):
        pass

    def setColour(self, colour: str):
        self.colour = colour

    def setSize(self, size: int):
        self.size = size

    def setText(self, text: str):
        self.text = text

    def draw(self):
        t = turtle.Turtle()
        t.color(self.colour)
        t.begin_fill()
        t.circle(self.size)
        t.end_fill()
        t.color("white")
        t.write(self.text, font=("arial", 10, "bold"), align="center")


b1 = Button()
b1.setColour("cyan")
b1.setSize(50)
b1.setText("hello there")
b1.draw()
b2 = Button()
b2.setColour("orange")
b2.setSize(10)
b2.setText("hi")
b2.draw()

turtle.exitonclick()
