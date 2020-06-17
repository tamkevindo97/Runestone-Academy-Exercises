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
        fred.forward(x[i])
        # technically i did not need to include these if,elif statements
        # since all y values are positive
        if y[i] > 0:
            fred.left(90)
            fred.forward(abs(y[i]))
            fred.dot()
            fred.home()
        elif y[i] < 0:
            fred.right(90)
            fred.forward(abs(y[i]))
            fred.dot()
            fred.home()
        else:
            fred.forward(abs(y[i]))
            fred.dot()
            fred.home()

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
        fred.forward(xplot[avalue])
        fred.left(90)
        fred.forward(yplot[avalue])
        fred.dot()
        fred.home()


# Create Screen
wn = turtle.Screen()
wn.tracer(10)
wn.setworldcoordinates(-100, -100, 100, 100)

# Create x and y axes
fred = turtle.Turtle()
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
