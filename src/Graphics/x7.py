from graphics import * 

def main(): 
    win = GraphWin("Where's Waldo", 200, 200)

    win.setCoords(
        -(win.getWidth() / 2),
        -(win.getHeight() / 2),
        (win.getWidth() / 2),
        (win.getHeight() / 2),
    )

    img = Image(Point(0,0), "cat.gif")

    print("Width", img.getWidth())
    print("Height", img.getHeight())
 
    img.draw(win)

    win.getMouse()
    win.close()
main()