from turtle import Turtle , done



t = Turtle()
def square(x, a):
    l = 1
    while l <= 4:
        t.forward(x)
        t.left()
        l += 1



square(50)




t.penup()
t.goto(100, 200)
t.pendown()
square(20)



done()