import turtle


class Artist:

    def __init__(self):
        screen = turtle.Screen()
        screen.bgcolor("black")

        self.t = turtle.Turtle()
        self.t.shape("turtle")
        self.t.color("aqua")

    def triangle(self, size:int = 100):
        self.polygon(3, size)

    def square(self, size:int = 100):
        self.polygon(4, size)
        
    def polygon(self, sideCount:int, size:int = 100):
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

def main():
    a = Artist()
    a.circle(500)

if __name__ == "__main__":
    main()
