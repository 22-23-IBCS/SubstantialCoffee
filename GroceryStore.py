
class Store:

    def __init__(self, inv:{}):
        self.inventory = inv

    def checkout(self, items: []):
        price = 0
        for item in items:
            if item in self.inventory:
                price += self.inventory[item]
        return price

    def getItems(self):
        return self.inventory

    def speakWithManager(self):
        print("what do you want...")
        input()
        print("eh whatever, go away")
        

def main():
    offers = {
        "dog": 1.91,
        "cat": 2.23,
        "sheep": 3.43,
        "hamster": 2.11,
        "fish": 20.43,
        "snake": 10.41,
        "bird": 12.94,
        "snail": 2.34,
        "crab": 39.23,
        "worm": 0.25
    }
    s = Store(offers)

    while True:

        for animal, price in s.getItems().items():
            print(animal + " -> " + str(price))
        items = input("what animals would you like to purchace? (press 1 to speak with the manager, and 2 to exit)\n")

        if len(items) == 1 and int(items) == 1:
            s.speakWithManager()
            continue

        if len(items) == 1 and int(items) == 2:
            return


        items = "".join(items.split()) #literally string.replace(" ", "") but doesn't work
        items = items.split(",")
        
        price = s.checkout(items)
        print("That will cost you " + str(price) + " dollars")


if __name__ == "__main__":
    main()
