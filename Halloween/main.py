import copy

from game.House import House
from game.graphics import GraphWin
from pathfinder.PathFinder import PathFinder


def find(houses: [], depth: int, dimension: ()):
    bestPath = None

    for x in range(dimension[0]):
        for y in range(dimension[1]):

            finder = PathFinder(copy.deepcopy(houses))
            path = finder.getOptimal(x, y, depth)

            if bestPath is None:
                bestPath = path
                continue

            if path.calcWeight() > bestPath.calcWeight():
                bestPath = path

    return bestPath


def main():
    win = GraphWin("Visualization", 500, 500)
    dimension = (7, 7)

    houses = []
    for i in range(dimension[0]):
        houses.append([])

    for x in range(dimension[0]):
        for y in range(dimension[1]):
            h = House(x, y, dimension[0], dimension[1])
            houses[x].append(h)

    for x in range(dimension[0]):
        for y in range(dimension[1]):
            house = houses[x][y]
            if x + 1 < dimension[0]:
                house.link(houses[x + 1][y])
            if x - 1 > -1:
                house.link(houses[x - 1][y])
            if y + 1 < dimension[1]:
                house.link(houses[x][y + 1])
            if y - 1 > -1:
                house.link(houses[x][y - 1])

    for l in houses:
        for house in l:
            house.draw(win)

    depth = input("How many houses: ")
    path = find(copy.deepcopy(houses), int(depth) - 1, dimension)
    path.draw(win)

    s = 0
    for l in houses:
        for house in l:
            s += house.getGenerous()
    s /= dimension[0] * dimension[1]

    print("Total Average: " + str(s))
    print("Path Average: " + str(path.calcWeight()))

    while True:
        pass


if __name__ == "__main__":
    main()
