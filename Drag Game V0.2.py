#on mouse press, keep drawing decreasing dots
# most important link 
# the docs: https://mcsp.wartburg.edu/zelle/python/graphics.py
from graphics import *
from time import sleep

class Dot(Circle):
    def __init__(self, center, radius):
        Circle.__init__(self, center, radius)


    def animateDraw(self, win):
        self.draw(win)
        self.setFill("white")


def main():
    win = GraphWin("My Game", 1500, 1000) # create a window
    t = Text(Point(80, 15), "Press 'Escape' to Quit") # create text
    t.draw(win) # draw text

    while win.checkKey() != "Escape": # while the esc key is not pressed
        point = win.checkMouse() # save the latest mouse click point 
        if point != None: # create and draw circle if this point exists
            dot = Dot((point), 50)
            dot.animateDraw(win)

    win.close() # Close window


if __name__ == "__main__":
    main()

# the more time goes for each second setFill to a more transparent colour, then undraw
# redraw?
# dot skal blive til en class hvor farven gradvist går fra sort til hvid
# alle punkter skal tegnes igen, hvis farven == hvid, så undraw
# using threads to redraw?
# med default autoflush bliver ændringer vist med det samme, så threads til ændringer?