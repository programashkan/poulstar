from turtle import Turtle, Screen, textinput
t = Turtle()

sc = Screen()
sc.setup(800, 200)
while True:
    x = textinput("queastsion", "enter number")
    x = int(x)
    t.forward(x)
    a = textinput("queastsion", "enter number")
    a =int(a)
    t.left(a)







