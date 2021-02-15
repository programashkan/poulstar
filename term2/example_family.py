from turtle import Turtle , done, Screen, textinput
from time import sleep

t=Turtle

import string, random
x = random.choice(string.ascii_letters)
print(x)

sc = Screen()
t = Turtle()

def go ():
    t.penup()
    t.forward(80)
    t.pendown()
sc.setup(480, 320)
sc.bgpic("family.png")
t.penup()
t.left(180)
t.forward(200)
t.left(-90)
t.forward(100)
t.pendown()
name = textinput(("نام"), x)
t.write(name)

def iu (a):
    if x not in a[0]:
        print("lose")
        sc.bye()



t.penup()
t.left(-90)
t.forward(100)
t.pendown()


def line():
    family = textinput(("فامیلی"), x)
    t.write(family)
    iu(family)
    go()

    city =textinput(("شهر"), x)
    t.write(city)
    iu(city)
    go()

    fruite = textinput(("میوه"), x)
    t.write(fruite)
    iu(fruite)
    go()


    th = textinput(("اشیا"), x)
    t.write(th)
    iu(th)
    go()


    cl = textinput(("رنگ"), x)
    t.write(cl)
    iu(cl)
    go()

line()








t.left(-90)
t.left(-90)
t.forward(540)

t.left(90)
t.forward(20)
t.left(90)
t.forward(50)
x = random.choice(string.ascii_letters)
print(x)
line()









done()









