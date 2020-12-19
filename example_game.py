from turtle import Turtle, Screen, textinput , done
t = Turtle()
t.speed(100)
sc = Screen()
sc.setup(1500, 1000)
sc.bgpic("background game 1.png")
t.penup()
t.left(90)
t.forward(310)
t.left(90)
t.forward(550)
t.left(180)
t.pendown()
t.speed(2)
t.forward(350)
t.left(-90)
t.forward(300)
x = textinput("witch way:", "enter number")
def way (u, d, b):
    if int(b) == u:
        sc.bgpic("download.png")
        print(str(d))

        sc.bye()



way(1, "game over", x)


way(2, "wrong way", x)

if int(x) == 3:
    print("nice")
    t.forward(120)
    t.left(90)
    t.forward(400)
    t.left(90)
    t.forward(370)
    t.left(-90)
    t.forward(250)

a = textinput("witch way:", "enter number")
way(1, "oh try again", a)

way(2, "nooooooo", a)


if int(a) == 3:
    print("bravo")
    t.forward(50)
    t.left(-90)
    t.forward(500)

c = textinput("witch way:", "enter number")

way(1, "congratulations" , c)

way(2, "not bad but lose", c)

way(3, "oh lose", c)






