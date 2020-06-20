import turtle
import random
import matplotlib.pyplot as plt

#
t = turtle.Turtle()

t.speed(0)
t.penup()
t.setposition(0,-100)
t.pendown()
t.pensize(3)
t.fillcolor("green")
t.begin_fill()
t.circle(100)
t.end_fill()
t.penup()
t.setposition(0,0)
t.pendown()
t.hideturtle()
t.color("yellow")
# t.penup()
# t.forward(50)
# t.pendown()
# t.circle(100)
# t.penup()
# t.backward(50)

def randommovement(startx=0,starty=0):
    t.pensize(1)
    t.setposition(startx,starty)
    maxdist=0
    for i in range(1000):
        x=(t.pos())[0]
        y=(t.pos())[1]
        if maxdist<((x-startx)**2+(starty-y)**2):
            maxdist = (x-startx)**2+(starty-y)**2
        while (x**2 + y**2 > 100**2):
            t.penup()
            if (x<0): x+=1
            else: x-=1
            if (y<0): y+=1
            else: y-=1
            t.setposition(x,y)
            t.pendown()
            continue
        t.forward(random.choice([0,0.5,1]))
        t.right(random.randrange(0,360))
    return (maxdist**0.5)

def randommovementgraph():
    turtle.tracer(0, 0)
    res={}
    for i in range(101):
        res[i]=0
    for i in range(100):
        a = int (randommovement())
        if a in list(res.keys()):
            res[a]+=1
        else:
            res[a]=1
    plt.bar(list(res.keys()), list(res.values()))
    plt.suptitle('times how many times walk ended at a certain distance\nwith starting position 0,0 (1000 steps)', fontsize=10)
    plt.xlabel('distances')
    plt.ylabel('no of times a walk ended')
    plt.show()


randommovement()
turtle.Screen().exitonclick()
