import turtle
import random
import math
#
t = turtle.Turtle()
c = turtle.Turtle()

t.speed(0)
t.penup()
t.setposition(0,-100)
t.pendown()
t.circle(100)
t.penup()
t.setposition(0,0)
t.pendown()
t.hideturtle()
t.color('blue')

c.speed(0)
c.penup()
c.setposition(0,-100)
c.pendown()
c.circle(100)
c.penup()
c.setposition(0,0)
c.pendown()
c.hideturtle()
c.color('red')

def randommovement():
    t.penup()
    c.penup()
    theta1= random.uniform(0,2*math.pi)
    theta2= random.uniform(0,2*math.pi)
    r1,r2 = random.randint(0,100),random.randint(0,100)
    t.setposition(r1 * float (math.cos(theta1)), r1* float (math.sin(theta1)))
    t.setposition(r2 * float(math.cos(theta2)), r2 * float(math.sin(theta2)))
    # t.setposition(0, 0)
    # c.setposition(1, 1)

    t.pendown()
    c.pendown()

    for i in range(999999999):
        x=(t.pos())[0]
        y=(t.pos())[1]
        while (x**2 + y**2 > 100**2):
            t.penup()
            if (x<0): x+=1
            else: x-=1
            if (y<0): y+=1
            else: y-=1
            t.setposition(x,y)
            t.pendown()
            continue

        a=(c.pos())[0]
        b=(c.pos())[1]
        while (a**2 + b**2 > 100**2):
            c.penup()
            if (a<0): a+=1
            else: a-=1
            if (b<0): b+=1
            else: b-=1
            c.setposition(a,b)
            c.pendown()
            continue

        distance = math.sqrt(((a - x) ** 2) + (b - y) ** 2)

        if (distance<1):
            print (i)

        t.forward(random.choice([0,0.5,1]))
        t.right(random.randint(0,360))

        c.forward(random.choice([0.5,0,1]))
        c.right(random.randint(0,360))




randommovement()






turtle.Screen().exitonclick()
