from turtle import Turtle, Screen, textinput

t = Turtle()
t.color("red")
t.pensize(10)
t.penup()
t.goto(-420, 420)
t.pendown()

sc = Screen()
sc.bgpic("1123.gif")
sc.setup(920, 920)
while True:
    x = textinput("forward", "enter number")
    x = int(x)
    t.forward(x)
    a = textinput("Angle", "enter number")
    a = int(a)
    t.left(a)
