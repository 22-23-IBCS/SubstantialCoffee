import random

from game.graphics import GraphWin, Circle, Point, Text, Line


class House:

    def __init__(self, x: int, y: int, totalX: int = 5, totalY: int = 5):
        self.generous = random.random() * 10

        self.x = x
        self.y = y

        self.totalX = totalX
        self.totalY = totalY

        self.neighbours = []

        self.visited = False

    def getGenerous(self):
        return self.generous

    def draw(self, win: GraphWin, color="white"):
        widthSpacing = win.getWidth() / (self.totalX + 1)
        heightSpacing = win.getHeight() / (self.totalY + 1)

        scaledX = widthSpacing * (self.x + 1)
        scaledY = heightSpacing * (self.y + 1)

        c = Circle(Point(scaledX, scaledY), 17)
        c.setFill(color)
        c.draw(win)

        t = Text(Point(scaledX, scaledY), str(round(self.generous, 3)))
        t.draw(win)

    def connect(self, win: GraphWin, other):
        widthSpacing = win.getWidth() / (self.totalX + 1)
        heightSpacing = win.getHeight() / (self.totalY + 1)

        scaledXA = widthSpacing * (self.x + 1)
        scaledYA = heightSpacing * (self.y + 1)

        scaledXB = widthSpacing * (other.x + 1)
        scaledYB = heightSpacing * (other.y + 1)

        p1 = Point(scaledXA, scaledYA)
        p2 = Point(scaledXB, scaledYB)

        line = Line(p1, p2)
        line.draw(win)

    def link(self, other):
        self.neighbours.append(other)

    def getNeighbours(self):
        self.visited = True
        return self.neighbours

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"
