from graphics import * 
from time import sleep 

win = GraphWin("Graphics Assignment 8", 1000, 1000)

"""
How could you make a character move using these methods?  On my website there are three sprites of a character (bomberman) moving.  Use the point and click method to cycle through these three images to show bomberman running.
"""

images = []
b1 = Image(Point(0,0), "bomberman1.gif")
b2 = Image(Point(0,0), "bomberman2.gif")
b3 = Image(Point(0,0), "bomberman3.gif")
images.append(b2)
images.append(b3)
images.append(b1)

def main(): 
    
    win.setCoords(
        -(win.getWidth() / 2),
        -(win.getHeight() / 2),
        (win.getWidth() / 2),
        (win.getHeight() / 2),
    )
    b1.draw(win)

    while True: 
        pt = win.getMouse()

        b1.undraw()
        b2.move((pt.getX() - b2.getAnchor().getX())/2, (pt.getY() - b2.getAnchor().getY())/2)
        b2.draw(win)
        sleep(1)
        b2.undraw()
        b3.move((pt.getX() - b3.getAnchor().getX()), (pt.getY() - b3.getAnchor().getY()))
        b3.draw(win)
        b1.anchor.x = b3.anchor.x
        b1.anchor.y = b3.anchor.y
        b1.draw(win)
        b3.undraw()
main()