class Point:
    def __init__(self, initx, inity):
        self.x = initx
        self.y = inity

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distancefrompoint(self, point):
        distx = point.x - self.x
        disty = point.y - self.y
        dist = (distx ** 2 + disty ** 2) ** (0.5)
        return "Distance from Point {0} to Point {1} is ".format(self.tostring(), point.tostring()) + str(dist)

    def tostring(self):
        return "({0},{1})".format(self.x, self.y)

p = Point(1, 2) # self point
q = Point(2, 4) # distance from this point
print(p.distancefrompoint(q))
