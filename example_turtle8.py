from turtle import Turtle
from random import randint

t= Turtle()

while True:
    t.penup()
    t.goto(randint(-250, 250), randint(-250, 250))
    t.pendown()
    t.speed(1000000)



    #color
    t.color("#" + str(randint(100000, 900000)))
    t.begin_fill()


    #TRIANGLE
    x = 1
    while x <+ 3:
        t.forward(100)
        t.left(120)
        x +=1


    t.end_fill()