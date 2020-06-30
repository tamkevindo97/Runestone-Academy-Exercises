labdata = open("labdata.txt", "r")
import turtle

# create a blank list for x and y values
xvalues = []
yvalues = []

# insert x and y values from labdata
for aline in labdata:
    values = aline.split()
    xvalues.append(int(values[0]))
    yvalues.append(int(values[1]))

print("x values: ", xvalues)
print("y values: ", yvalues)

def plotRegression(x, y):
    for i in range(len(x)):
        fred.penup()
        fred.goto(x[i], y[i])
        fred.dot()

    # initialize sums for forloop
    sumxy = 0
    sumxsquared = 0
    yplot = []

    for p in range(len(x)):
        # means of x and y are required in both y and m equations
        xmean = sum(x)
        ymean = sum(y)
        # sums are required in m equation
        sumxy = sumxy + x[p] * y[p]
        sumxsquared = sumxsquared + x[p] ** 2
        # m equation is given
        m = (sumxy - (len(x)) * xmean * ymean) / (sumxsquared - ((len(x)) * (xmean ** 2)))
        # x values are given, plug x into y equation
        xplot = x
        yplot.append(ymean + m * (xplot[p] - xmean))

    # plotting best fit line using x values and y equation
    print("xplot values ", xplot)
    print("yplot values ", yplot)
    fred.pencolor("red")
    for avalue in range(len(xplot)):
        fred.penup()
        fred.goto(xplot[avalue], yplot[avalue])
        fred.dot()

# Create Screen
wn = turtle.Screen()

wn.setworldcoordinates(-100, -100, 100, 100)

# Create x and y axes
fred = turtle.Turtle()
fred.speed(8)
fred.forward(100)
fred.backward(200)
fred.home()
fred.left(90)
fred.forward(100)
fred.backward(200)
fred.home()

# Call plotRegression
plotRegression(xvalues, yvalues)

wn.exitonclick()
labdata.close()
