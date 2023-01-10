from graphics import *;win = GraphWin("Boxes and Ovals", 200, 200);win.setBackground("grey");win.setCoords(0.0, 0.0, 3.0, 3.0);Line(Point(1, 0), Point(1, 3)).draw(win);Line(Point(2, 0), Point(2, 3)).draw(win);Line(Point(0, 1), Point(3, 1)).draw(win);Line(Point(0, 2), Point(3, 2)).draw(win);turn = 0
def draw(*points: Point):
    global turn
    if turn == 0: Oval(points[0], points[1]).draw(win).setFill("green");turn = 1
    else: Rectangle(points[2], points[3]).draw(win).setFill("red");turn = 0
def current():
    if turn == 1: return "Oval"
    else: return "Square"
class Board:
    def __init__(self):
        Board.top = {"left": "", "middle": "", "right": ""}
        Board.middle = {"left": "", "middle": "", "right": ""}
        Board.bottom = {"left": "", "middle": "", "right": ""}
    def update(self, row, column, new):
        if row == "top": Board.top[column] = new;Board.top = Board.top 
        if row == "middle": Board.middle[column] = new;Board.middle = Board.middle
        if row == "bottom": Board.bottom [column] = new;Board.bottom = Board.bottom
    def checkWinner(self): 
        if (Board.top["left"] and Board.top["left"] == Board.top["middle"] and Board.top['left'] == Board.top["right"]): return f'{Board.top["left"]} is the winner!'
        if (Board.middle["left"] and Board.middle["left"] == Board.middle["middle"] and Board.middle['left'] == Board.middle["right"]): return f'{Board.middle["left"]} is the winner!'
        if (Board.bottom["left"] and Board.bottom["left"] == Board.bottom["middle"] and Board.bottom['left'] == Board.bottom["right"]): return f'{Board.bottom["left"]} is the winner!'
        if (Board.top["left"] and Board.top["left"] == Board.middle["left"] and Board.top["left"] == Board.bottom["left"]): return f'{Board.top["left"]} is the winner!'
        if (Board.top["middle"] and Board.top["middle"] == Board.middle["middle"] and Board.top["middle"] == Board.bottom["middle"]): return f'{Board.top["middle"]} is the winner!'
        if (Board.top["right"] and Board.top["right"] == Board.middle["right"] and Board.top["right"] == Board.bottom["right"]): return f'{Board.top["right"]} is the winner!'
        if (Board.top["left"] and Board.top["left"] == Board.middle["middle"] and Board.top["left"] == Board.bottom["right"]): return f'{Board.top["left"]} is the winner!'
        if (Board.top["right"] and Board.top["right"] == Board.middle["middle"] and Board.top["right"] == Board.bottom["left"]): return f'{Board.top["right"]} is the winner!'
        else: return ""
b = Board()
moves = 9
playing = True

while playing == True: 
    for i in range(moves):
        p = win.getMouse()
        if p.getX() < 1:
            if p.getY() < 1:  # column1, row1
                if (b.bottom["left"]): moves = moves + 1;continue
                else: draw(Point(0, 0), Point(1, 1), Point(0.1, 0.1), Point(0.9, 0.9));b.update("bottom", "left", current())
            if p.getY() < 2 and p.getY() > 1:
                if (b.middle["left"]): moves = moves + 1;continue
                else: draw(Point(0, 1), Point(1, 2), Point(0.1, 1.1), Point(0.9, 1.9));b.update("middle", "left", current())
            if p.getY() < 3 and p.getY() > 2:
                if (b.top["left"]): moves = moves + 1;continue
                else: draw(Point(0, 2), Point(1, 3), Point(0.1, 2.1), Point(0.9, 2.9));b.update("top", "left", current())
        if p.getX() < 2 and p.getX() > 1:
            if p.getY() < 1:
                if (b.bottom["middle"]): moves =  moves + 1;continue
                else: draw(Point(1, 0), Point(2, 1), Point(1.1, 0.1), Point(1.9, 0.9));b.update("bottom", "middle", current())
            if p.getY() < 2 and p.getY() > 1:
                if (b.middle["middle"]): moves = moves + 1;continue
                else: draw(Point(1, 1), Point(2, 2), Point(1.1, 1.1), Point(1.9, 1.9));b.update("middle", "middle", current())
            if p.getY() < 3 and p.getY() > 2:
                if (b.top["middle"]): moves = moves + 1;continue
                else:draw(Point(1, 2), Point(2, 3), Point(1.1, 2.1), Point(1.9, 2.9));b.update("top", "middle", current())
        if (p.getX() < 3) and p.getX() > 2:
            if p.getY() < 1:
                if (b.bottom["right"]): moves = moves + 1;continue
                else: draw(Point(2, 0), Point(3, 1), Point(2.1, 0.1), Point(2.9, 0.9));b.update("bottom", "right", current())
            if p.getY() < 2 and p.getY() > 1:
                if (b.middle["right"]): moves = moves + 1;continue
                else: draw(Point(2, 1), Point(3, 2), Point(2.1, 1.1), Point(2.9, 1.9));b.update("middle", "right", current())
            if p.getY() < 3 and p.getY() > 2:
                if (b.top["right"]): moves = moves + 1;continue
                else: draw(Point(2, 2), Point(3, 3), Point(2.1, 2.1), Point(2.9, 2.9));b.update("top", "right", current())
        print(b.top);print(b.middle);print(b.bottom);res = b.checkWinner();print(res)
        if (res): playing = False;break
win.getMouse();win.close()