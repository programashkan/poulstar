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


    t.circle(50)
    t.end_fill()