import turtle

def drawSquare(t,sz):
    for i in range(2):
        t.forward(sz/2)
        t.left(90)
        t.forward(sz)
        t.left(90)
        t.forward(sz/2)
def multipleSquare(u,tz):
    count = 20
    for i in range(10):
        drawSquare(u,tz + count)
        u.penup()
        u.right(90)
        u.forward(10)
        u.left(90)
        u.pendown()
        count = count + 20

def main():
    wn = turtle.Screen()
    wn.bgcolor("green")
    alex = turtle.Turtle()
    alex.color("pink")
    alex.pensize(3)
    multipleSquare(alex,0)

main()
