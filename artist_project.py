import turtle


class Artist:

    def __init__(self):
        screen = turtle.Screen()
        screen.bgcolor("black")

        self.t = turtle.Turtle()
        self.t.shape("turtle")
        self.t.color("aqua")
        self.t.speed(0)

    def triangle(self, size:int = 100):
        self.polygon(3, size)

    def square(self, size:int = 100):
        self.polygon(4, size)
        
    def polygon(self, sideCount:int, size:float = 100):
        angle:int = self.getAngle(sideCount)
        for i in range(sideCount):
            self.t.forward(size)
            self.t.right(angle)

    def star(self, size:int = 100):
        for i in range(5):
            self.t.forward(size)
            self.t.right(144)

    def circle(self, size:int = 100):
        self.polygon(size, 1)
    
    def getAngle(self, vertex:int):
        return 180 - ((vertex-2)*180/vertex)


    def customA(self):
        for i in range(3, 10):
            self.polygon(i, 50)

    def customB(self):
        for i in range(420):
            self.t.forward(50)
            self.t.right(69)

def main():
    a = Artist()
    a.customB()

if __name__ == "__main__":
    main()
