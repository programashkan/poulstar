from turtle import Turtle , done



t = Turtle()
def square(x):
    l = 1
    while l <= 4:
        t.forward(x)
        t.left(90)
        l += 1



square(60)




t.penup()
t.goto(100, 200)
t.pendown()
square(100)



done()