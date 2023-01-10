from graphics import * 
from time import sleep
def clicked(button: Rectangle, click: Point):
    P1: Point = button.getP1()
    P2: Point = button.getP2()
    if (P1.x >= 0): 
        if click.getX() >= P1.getX() and click.getX() <= P2.getX(): 
            if (P2.y > 0): 
                if click.getY() >= P1.getY() and click.getY() <= P2.getY():return True
                else: return False
            else: 
                if click.getY() <= P1.getY() and click.getY() >= P2.getY(): return True
                else: return False
        else: return False
    if (P1.x < 0): 
        if click.getX() >= P1.getX() and click.getX() <= P2.getX(): 
            if (P2.y > 0):
                if click.getY() >= P1.getY() and click.getY() <= P2.getY():return True
                else: return False
            else: 
                if click.getY() <= P1.getY() and click.getY() >= P2.getY(): return True
                else: return False
        else: return False
left=[Image(Point(0,0), "bomberman1left.gif"), Image(Point(0,0), "bomberman2left.gif"), Image(Point(0,0), "bomberman3left.gif")]
right=[Image(Point(0,0), 'bomberman1.gif'), Image(Point(0,0), "bomberman2.gif"), Image(Point(0,0), "bomberman3.gif")]
direction = "right"
def main():
    global direction
    win = GraphWin("XX2 - Part 2 (Create buttons)", 500, 500);win.setCoords(-(win.getWidth() / 2),-(win.getHeight() / 2),(win.getWidth() / 2),(win.getHeight() / 2),);Text(Point(-100, 240), "Left").draw(win);leftButton = Rectangle(Point(-120, 230), Point(-80, 250)).draw(win);Text(Point(100, 240), "Right").draw(win);rightButton = Rectangle(Point(80, 230), Point(120, 250)).draw(win);Text(Point(0, 240), "Shoot").draw(win);shootButton = Rectangle(Point(-20, 230), Point(20, 250)).draw(win);bomberman = Image(Point(0,0), "bomberman1.gif").draw(win)
    while True: 
        click = win.getMouse();leftClicked = clicked(leftButton, click);rightClicked = clicked(rightButton, click);shootClicked = clicked(shootButton, click);print("Left clicked?: ", leftClicked);print("Right Clicked?: ", rightClicked);print("Shoot clicked?: ", shootClicked)
        if (leftClicked): 
            direction = "left"
            for i in range(3): 
                    img = left[i]
                    img.anchor.x = bomberman.anchor.x
                    img.anchor.y = bomberman.anchor.y
                    bomberman.undraw()
                    img.draw(win)
                    bomberman = img
                    img.move(-5,0)
                    sleep(.5)
                    if (i == 2): continue
                    else: img.undraw()
        if (rightClicked): 
            direction = "right"
            for i in range(3): 
                    img = right[i]
                    img.anchor.x = bomberman.anchor.x
                    img.anchor.y = bomberman.anchor.y
                    bomberman.undraw()
                    img.draw(win)
                    bomberman = img
                    img.move(5, 0)
                    sleep(.5)
                    if (i == 2): continue
                    else: img.undraw()
        if (shootClicked): 
            bullet = Circle(Point(bomberman.anchor.x, bomberman.anchor.y), 5).draw(win);bullet.setOutline("red");bullet.setFill("red")
            while bullet.p1.x <= 250: 
                    if (direction == "right"): 
                        bullet.move(10, 0)
                        time.sleep(0.1)
                    else: 
                        bullet.move(-10, 0)
                        time.sleep(0.1)
                    if (bullet.getCenter().x >= 250): break
                    if (bullet.getCenter().x <= -250): break
            bullet.undraw()
            continue
main()