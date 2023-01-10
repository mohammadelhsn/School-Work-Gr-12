from graphics import * 
from time import sleep
def clicked(button:Rectangle,click:Point):
    P1:Point=button.getP1();P2: Point=button.getP2()
    if(P1.x>=0): 
        if(click.getX()>=P1.getX() and click.getX()<=P2.getX()): 
            if (P2.y > 0): 
                if(click.getY()>=P1.getY() and click.getY()<=P2.getY()):return True
                else:return False
            else: 
                if(click.getY()<=P1.getY() and click.getY() >= P2.getY()):return True
                else:return False
        else:return False
    if(P1.x<0): 
        if(click.getX()>=P1.getX() and click.getX()<=P2.getX()): 
            if(P2.y > 0):
                if(click.getY() >= P1.getY() and click.getY() <= P2.getY()):return True
                else:return False
            else: 
                if(click.getY() <= P1.getY() and click.getY() >= P2.getY()):return True
                else:return False
        else:return False
drawn=True;direction="right";left=[Image(Point(0,0),"bomberman1left.gif"),Image(Point(0,0),"bomberman2left.gif"),Image(Point(0,0),"bomberman3left.gif")];right=[Image(Point(0,0),'bomberman1.gif'),Image(Point(0,0),"bomberman2.gif"),Image(Point(0,0),"bomberman3.gif")]
holes_right = []
holes_left = []
def main():
    global drawn;global direction;win=GraphWin("xx2",500,500);win.setCoords(-(win.getWidth()/2),-(win.getHeight()/2),(win.getWidth()/2),(win.getHeight()/2),);Text(Point(-100,240),"Left").draw(win);leftButton=Rectangle(Point(-120,230),Point(-80,250)).draw(win);Text(Point(100,240),"Right").draw(win);rightButton=Rectangle(Point(80,230),Point(120,250)).draw(win);Text(Point(0,240),"Shoot").draw(win);shootButton=Rectangle(Point(-20,230),Point(20,250)).draw(win);bomberman=Image(Point(0,0),"bomberman1.gif").draw(win);left_wall=Rectangle(Point(-250,-250),Point(-230,250)).draw(win);right_wall=Rectangle(Point(230,-250),Point(250,250)).draw(win);left_wall.setFill("red");left_wall.setOutline("black");right_wall.setFill("red");right_wall.setOutline("black");Text(Point(-175, 240), "Up").draw(win);upButton=Rectangle(Point(-200, 230), Point(-150, 250)).draw(win);Text(Point(175, 240), "Down").draw(win);downButton=Rectangle(Point(150, 230), Point(200, 250)).draw(win)
    while True: 
        try: 
            click = win.getMouse();print(click);leftClicked = clicked(leftButton, click);rightClicked = clicked(rightButton, click);shootClicked = clicked(shootButton, click);upClicked=clicked(upButton, click);downClicked=clicked(downButton, click);print("Left clicked?: ", leftClicked);print("Right Clicked?: ", rightClicked);print("Shoot clicked?: ", shootClicked);print("Up clicked?: ", upClicked);print("Down clicked?: ", downClicked)
            if (leftClicked): 
                if((bomberman.anchor.x-10-(bomberman.getWidth()/2))<=-230):continue 
                else: 
                    direction="left"
                    for i in range(3): 
                        img=left[i];img.anchor.x=bomberman.anchor.x;img.anchor.y=bomberman.anchor.y;bomberman.undraw();img.draw(win);bomberman=img;img.move(-5,0);sleep(.5)
                        if(i==2):continue
                        else:img.undraw()
            if (rightClicked): 
                if ((bomberman.anchor.x + 10 + (bomberman.getWidth() / 2)) >= 230):
                    ys = []
                    for hole in holes: 
                        print(hole)
                else: 
                    direction = "right"
                    for i in range(3): 
                        img=right[i];img.anchor.x=bomberman.anchor.x;img.anchor.y=bomberman.anchor.y;bomberman.undraw();img.draw(win);bomberman=img;img.move(5, 0);sleep(.5)
                        if(i == 2): continue
                        else:img.undraw()
            if (upClicked): 
                if ((bomberman.anchor.y + 10 + (bomberman.getHeight()/2)) >= 230): continue
                else: 
                    bomberman.move(0,10)
            if(downClicked): 
                if ((bomberman.anchor.y - 10 - (bomberman.getHeight()/2)) <= -230): continue
                else: 
                    bomberman.move(0, -10)
            if(shootClicked): 
                bullet = Circle(Point(bomberman.anchor.x, bomberman.anchor.y), 5).draw(win);bullet.setOutline("lime");bullet.setFill("lime")
                drawn=True
                while bullet.p1.x<=250: 
                    if(direction=="right"): bullet.move(10, 0);time.sleep(0.1)
                    else:bullet.move(-10,0);time.sleep(0.1)
                    if(bullet.getCenter().x==240):drawn=False;print(bullet.p1);print(bullet.p2);holes_right.append(Circle(bullet.getCenter(), 10).draw(win));break
                    if(bullet.getCenter().x==-240):drawn=False;print(bullet.p1);print(bullet.p2);holes_left.append(Circle(bullet.getCenter(), 10).draw(win));break
                if (drawn!=True):bullet.undraw()
                print(holes_right)
                print(holes_left)
                for hole in holes_right: 
                    h: Circle = hole
                    h.setFill("white")
                    h.setOutline("white")
                    h.setWidth(5)
                for hole in holes_left: 
                    h: Circle = hole
                    h.setFill("white")
                    h.setOutline("white")
                    h.setWidth(5)

                continue
        except Exception as e: win.close()
main()
"""
Have bomberman move up and down, and give the ability to shoot the wall - collision detection is still working on each wall.  Each time bomberman hits the wall, 
take a small piece out of it when the laser hits it.  When the hole is big enough, bomberman should be able to fit through
"""