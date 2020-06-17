class Point:
    def __init__(self, xpoint, ypoint):
        self.x = xpoint
        self.y = ypoint

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distfromorigin(self):
        return "Distance = " + str(((self.x**2) + (self.y**2))**(1/2))

    def string(self):
        return "x = " + str(self.x) + " y = " + str(self.y)

a = Point(3, 4)
print(a.distfromorigin())
print(a.string())
