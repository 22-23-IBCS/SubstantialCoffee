

class Animal:

    def __init__(self, animalType:str, size:int, speed:float, food:str):
        self.animalType = animalType
        self.size = size
        self.speed = speed
        self.food = food

    def getType(self):
        return self.animalType

    def getSize(self):
        return self.size

    def getSpeed(self):
        return self.speed

    def getFood(self):
        return self.food

    def setType(self, animalType:str):
        self.animalType = animalType

    def setSize(self, size:int):
        self.size = size

    def setSpeed(self, speed:float):
        self.speed = speed

    def setFood(self, food:str):
        self.food = food

    def eat(self):
        print("chomp chomp chomp")

    def run(self):
        print("I am running at speed " + str(self.speed))
    


def main():
    animalA = Animal("cheetah", 2, 60, "deer")
    
    print(animalA.getSpeed())
    print(animalA.getFood())
    
    animalA.run()
    animalA.eat()

    animalB = Animal("house cat", 1, 30, "mouse")
    print(animalB.getSpeed())
    print(animalB.getFood())

    animalB.setFood("bird")
    print(animalB.getFood())
    

if __name__ == "__main__":
    main()
