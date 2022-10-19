from game.House import House
from game.graphics import GraphWin


class Path:

    def __init__(self):
        self.houses = []

    def addHouse(self, house: House):
        self.houses.append(house)
        return self

    def calcWeight(self):
        total = 0
        for house in self.houses:
            total += house.getGenerous()

        if len(self.houses) == 0:
            return 0

        return total / len(self.houses)  # Gets the average value

    def draw(self, win: GraphWin):
        for house in self.houses:
            house.draw(win, "red")

        for i in range(len(self.houses) - 1):
            self.houses[i].connect(win, self.houses[i+1])

