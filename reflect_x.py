import random
class Point:
    def __init__(self, initx, inity):
        self.x = initx
        self.y = inity

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def tostring(self):
        return "({0},{1})".format(self.x, self.y)

    def reflect_x(self):
        new_x = self.x * -1
        reflectedpt = Point(new_x, self.y)
        return "The reflected point of {0} across the x-axis is {1}".format(self.tostring(), reflectedpt.tostring())

x_input = input("Enter any x value: ")
y_input = input("Enter any y value: ")
p = Point(int(x_input), int(y_input))
print(p.reflect_x())