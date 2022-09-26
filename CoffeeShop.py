class CoffeeShop:

    # drinks is list of Strings
    def __init__(self, drinks: {}, prices: {}):
        self.drinks = drinks
        self.prices = prices
        print("Welcome to the Coffee Shop")

    def manageOrder(self):
        print("1. Order")
        print("2. Learn more about the store!")

        while True:
            inputValue: int = int(input())
            if inputValue == 1:
                print("Drink Numbers: ")
                for num, drink in self.drinks.items():
                    print(str(num) + " -> " + str(drink) + " (" + str(self.prices[drink]) + ")")
                self.order(int(input("Enter the number of the drink you would like to order: ")))
                return
            elif inputValue == 2:
                print("The Coffee shop lets you order coffee through your computer!  Wonderful :D")
                return
            else:
                print("invalid input")

    def order(self, orderNum: int):
        while True:
            if orderNum in self.drinks:
                name: str = input("Could I get a name for that?\n")
                print("One " + self.drinks[orderNum] + " for " + name + " for a price of " + self.prices[
                    self.drinks[orderNum]
                ])
                return
            else:
                print("Invalid order")
                self.manageOrder()


def main():
    shop = CoffeeShop({
        1: "coffee",
        2: "latte",
        3: "hot cider",
        4: "mocha"
    },
        {
            "coffee": "$4:00",
            "latte": "$6:00",
            "hot cider": "$4.50",
            "mocha": "$5.00"
        })

    shop.manageOrder()


if __name__ == "__main__":
    main()
