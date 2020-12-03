from turtle import Turtle , done



t = Turtle()
def square():
    l = 1
    while l <= 4:
        t.forward(100)
        t.left(90)
        l += 1
def triangle():
    e= 1
    while e <= 3:
        t.forward(100)
        t.left(120) 



square()
triangle()



t.penup()
t.goto(100, 200)
t.pendown()
square()



done()