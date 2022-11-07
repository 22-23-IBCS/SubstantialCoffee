from graphics import *

class Button(Rectangle):

    def __init__(self, a: Point, b: Point, win: GraphWin, color, text):
        super().__init__(a, b)
        super().draw(win)
        super().setFill(color)
        self.a = a
        self.b = b

        self.minX = self.a.getX()
        self.maxX = self.b.getX()
        self.minY = self.a.getY()
        self.maxY = self.b.getY()

        self.text = Text(Point((self.minX + self.maxX)/2, (self.minY + self.maxY)/2), text)
        self.text.draw(win)

    
    def isClicked(self, p: Point):
        if self.minX < p.getX() < self.maxX:
            if self.minY < p.getY() < self.maxY:
                return True
        return False


def main():
    win = GraphWin("hi")
    a = Button(Point(0,0), Point(50, 100), win, "red", "hi there")
    while True:
        m = win.getMouse()
        if a.isClicked(m):
            print("ayo")

if __name__ == "__main__":
    main()
