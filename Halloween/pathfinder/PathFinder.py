import copy

from pathfinder.Path import Path


class PathFinder:

    def __init__(self, houses: []):
        self.houses = houses  # list of houses properly linked

    def getOptimal(self, x: int, y: int, depth: int, path: Path = Path()):  # -> Path
        path = copy.deepcopy(path)
        if len(path.houses) == 0:
            path.addHouse(self.houses[x][y])

        currBest = Path()

        if depth == 0:
            return path

        neighbours = self.houses[x][y].getNeighbours()

        if len(neighbours) == 0:
            return -1

        for house in neighbours:
            if house.visited:
                continue

            testPath = copy.deepcopy(path)
            current = self.getOptimal(house.x, house.y, depth - 1, testPath.addHouse(house))

            for h in current.houses:
                h.visited = False

            if current.calcWeight() > currBest.calcWeight():
                currBest = current

        return copy.deepcopy(currBest)
