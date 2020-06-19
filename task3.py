import turtle
import random
#
t = turtle.Turtle()

t.speed(0)
t.penup()
t.setposition(0,-100)
t.pendown()
t.circle(100)
t.penup()
t.setposition(0,0)
t.pendown()
t.hideturtle()
# t.penup()
# t.forward(50)
# t.pendown()
# t.circle(100)
# t.penup()
# t.backward(50)

def randommovement():
    t.pensize(1)
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
        t.forward(random.choice([0,0.5,1]))
        t.right(random.randrange(0,360))


randommovement()






turtle.Screen().exitonclick()
