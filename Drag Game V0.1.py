#on mouse press, keep drawing decreasing dots
# most important link 
# the docs: https://mcsp.wartburg.edu/zelle/python/graphics.py
from graphics import *

class Dot(Circle):
    def __init__(self, center, radius, life = 1):
        Circle.__init__(self, center, radius)
        self.setFill("black")
        self.life = life

    def redraw(self):
        self.radius **= 0.9 # making the radius exponentially smaller
        self.undraw()

def main():
    win = GraphWin("My Game", 1500, 1000) # create a window
    t = Text(Point(80,15), "Press Escape to Quit")
    t.draw(win)

    while True:
        # if the mouse is pressed draw a circle at coords
        point = win.checkMouse()

        if point != None:
            dot = Dot((point), 50)
            dot.draw(win)

        if win.checkKey() == "Escape":
            win.close()    # Close window


if __name__ == "__main__":
    main()

# the more time goes for each second setFill to a more transparent colour, then undraw
# redraw?
# dot skal blive til en class hvor farven gradvist går fra sort til hvid
# alle punkter skal tegnes igen, hvis farven == hvid, så undraw
# using threads to redraw?
# med default autoflush bliver ændringer vist med det samme, så threads til ændringer?