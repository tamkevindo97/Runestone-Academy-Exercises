import turtle  # import modules
import math
import random

wn = turtle.Screen()  # create window
wn.setworldcoordinates(-1, -1, 1, 1)  # coordinates of window
wn.tracer(10)  # speed of pen
wn.title("Darts Simulation")
fred = turtle.Turtle()  # create a turtle named "fred"

numdarts = 1000  # number of darts
# lines 12-16: start from the bottom of window
fred.home()
count = 0
for i in range(0, 6):
    fred.circle(count)
    fred.penup()
    fred.right(90)
    fred.forward(0.2)
    fred.left(90)
    fred.pendown()
    count = count + 0.2

fred.penup()  # pen is now up
fred.home()  # bring fred back to the origin
count2 = 0
count4 = 0
count6 = 0
count8 = 0
count10 = 0
count0 = 0
for i in range(numdarts):  # create numdarts amount of darts
    randx = random.random() * (-2) + 1  # x location of dart
    randy = random.random() * (-2) + 1  # y location of dart
    fred.forward(randx)  # move fred x depending on negative or positive
    if randy > 0:  # move fred y depending on negative or positive
        fred.left(90)
        fred.forward(abs(randy))
    else:
        fred.right(90)
        fred.forward(abs(randy))
    if  fred.distance(0,0) < 0.2:
        fred.pencolor("red")
        count2 = count2 + 1
    elif fred.distance(0,0) < 0.4:
        fred.pencolor("orange")
        count4 = count4 + 1
    elif fred.distance(0,0) < 0.6:
        fred.pencolor("gold")
        count6 = count6 + 1
    elif fred.distance(0,0) < 0.8:
        fred.pencolor("light green")
        count8 = count8 + 1
    elif fred.distance(0,0) < 1.0:
        fred.pencolor("light blue")
        count10 = count10 + 1
    else:
        fred.pencolor("purple")
        count0 = count0 + 1

    fred.dot()  # plate dot on the x,y position
    fred.penup()  # pen is now up
    fred.home()  # bring fred back to origin and repeat forloop for next iteration

total = count2+count4+count6+count8+count10+count0

print("There are ", count2, "darts within 0.2 from the origin")
print("There are ", count4, "darts within 0.4 from the origin")
print("There are ", count6, "darts within 0.6 from the origin")
print("There are ", count8, "darts within 0.8 from the origin")
print("There are ", count10, "darts within 1.0 from the origin")
print("There are ", count0, "darts outside of 1.0")

if total == numdarts:
    print("Pass: The sum of counters equal to the number of input darts")
else:
    print("No Pass: The sum of counters do not equal to the number of input darts")

wn.exitonclick()
