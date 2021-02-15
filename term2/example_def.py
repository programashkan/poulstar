from turtle import Turtle , done



t = Turtle()
def square():
    l = 1
    while l <= 4:
        t.forward(100)
        t.left(90)
        l += 1



square()




t.penup()
t.goto(100, 200)
t.pendown()
square()



done()