import turtle


class Button:
    colour: str
    size: int
    text: str
    def __init__(self, colour, size, text):
        self.colour = colour
        self.size = size
        self.text = text
    def draw(self):
        t = turtle.Turtle()
        t.color(self.colour)
        t.begin_fill()
        t.circle(self.size)
        t.end_fill()
        t.color("white")
        t.write(self.text, font=("arial", 10, "bold"), align="center")


b1 = Button("cyan",50,"hello there")
b1.draw()
b2 = Button("orange",10,"hi")
b2.draw()

turtle.exitonclick()
