from turtle import Turtle , done

t = Turtle()
#step 1
t.color("black")
t.begin_fill()
t.speed(200000000)



d = 1
while d <= 38:
    t.forward(10)
    t.left(5)

    d += 1
a = 1
while a<= 20:
    t.forward(10)
    t.left(10)
    a += 1
p = 1
t.penup()
while p <= 15:
    t.forward(10)
    t.left(10)
    p +=1


t.end_fill()
#step 2


s = 1
while s <= 37:
    t.forward(10)
    t.left(5)
    s += 1
t.pendown()
t.color("white")
t.begin_fill()
r = 1
while r <= 18:
    t.forward(10)
    t.left(10)
    r +=1
# circle 1
t.end_fill()
t.penup()
t.color("white")
t.begin_fill()
t.goto(5, 200)
t.pendown()
t.circle(10)
t.end_fill()



#circle 2
t.color("black")
t.begin_fill()
t.penup()
t.goto(-5, 50)
t.pendown()
t.circle(10)
t.end_fill()
t.penup()
t.goto(20 , 500)













done()