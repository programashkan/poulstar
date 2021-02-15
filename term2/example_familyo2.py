from turtle import Terminator, Turtle, done , Screen , textinput
#SCREEN
sc = Screen()
t = Turtle()
sc.setup(1100,1000)
t.speed(100000)
t.forward(350)
t.left(90)
t.forward(350)
t.left(90)


# RANDOM LETTER 01
import string, random
x = random.choice(string.ascii_letters)
print(x)


t.write("نام", font=("Verdana",25, "normal"))


#تابع فونت نوشتن


def name (a):
    t.forward(150)
    t.write(str(a), font=("Verdana",25, "normal"))

score = 60
# DEF LOSE OR WIN
def iu (a):
    if x not in a[0]:
        sc.bye()



        


# GAME SCREEN
name("فامیلی")
name("شهر")
name("میوه")
name("اشیا")
name("رنگ")
t.left(90)
t.forward(350)
t.left(90)
t.forward(400)
t.forward(200)
t.left(90)
t.forward(350)

t.left(90)
t.forward(150)
t.left(90)
t.forward(350)
t.left(90)
t.forward(-150)
t.left(90)
t.forward(350)
t.left(90)
t.forward(150)
t.left(90)
t.forward(350)
t.left(90)
t.forward(750)
t.left(-90)
t.forward(-350)
t.left(-90)
t.forward(150)


# DEF GO
def go ():
    t.penup()
    t.forward(150)
    t.pendown()


#DEF WRITE
def write (a):
    t.write(a , font=("Verdana", 10, "normal"))


#DEF ALL
def line():
    name = textinput(("نام"), x)
    write(name)
    iu(name)
    go()





    family = textinput(("فامیلی"), x)
    write(family)
    iu(family)
    go()

    city =textinput(("شهر"), x)
    write(city)
    iu(city)
    go()

    fruite = textinput(("میوه"), x)
    write(fruite)
    iu(fruite)
    go()


    th = textinput(("اشیا"), x)
    write(th)
    iu(th)
    go()


    cl = textinput(("رنگ"), x)
    write(cl)
    iu(cl)
    go()



#SCREEN
t.penup()
t.left(90)
t.forward(20)
t.left(-90)
t.forward(-80)
t.pendown()

line()
print(score)





t.penup()
t.left(90)
t.forward(50)
t.left(90)
t.forward(980)
t.left(-180)
t.forward(50)
t.pendown()


#RANDOM LETTER 02
import string, random
x = random.choice(string.ascii_letters)
print(x)
line()




done()