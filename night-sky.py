import turtle
import random

count = 10

t = turtle.Turtle()
t.pensize(5)

def star(size):
    for j in range(5):
        t.forward(size)
        t.right(144)

# t.penup()
# t.goto(222,44)
# t.down()
# star()

# t.penup()
# t.goto(122,104)
# t.down()
# star()


def drawStart(a,b,mycolor,size):
    t.pencolor(mycolor)
    t.color(mycolor)
    t.penup()
    t.goto(a,b)
    t.pendown()
    t.begin_fill()
    star(size)
    t.end_fill()

# drawStart(122,35,"blue",45)
# drawStart(222,35,"red",30)
# drawStart(22,135,"yellow",60)
# drawStart(322,55,"orange",25)
# drawStart(272,235,"white",85)

def randomXY():
    rangeX = (-300,300)
    rangeY = (0,400)

    x = random.randint(-300,300)
    y = random.randint(0,400)

    return x,y


def randomSize():
    rangeX = (20,60)

    x = random.randrange(*rangeX)
    
    return x

# x,y = randomXY()
# drawStart(x,y,"blue",randomSize())
# x,y = randomXY()
# drawStart(x,y,"yellow",randomSize())
# x,y = randomXY()
# drawStart(x,y,"orange",randomSize())
# x,y = randomXY()
# drawStart(x,y,"white",randomSize())

for i in range(3):
    for j in ['red','blue','green','orange','yellow','pink','skyblue']:
        x,y = randomXY()
        drawStart(x,y,j,randomSize())



turtle.done()