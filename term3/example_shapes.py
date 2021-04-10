from tkinter import *
from turtle import Turtle

# ─── VARIABLE ───────────────────────────────────────────────────────────────────



# ─── FUANCTION ──────────────────────────────────────────────────────────────────
t = Turtle()
def circle():
    t.circle(50)
def press():
    global f
    f = x.get()
    print(f)


def square():
    
    t.forward(f)
    t.left(90)
    t.forward(f)
    t.left(90)
    t.forward(f)
    t.left(90)
    t.forward(f)
    t.left(90)
def rectangle():
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.left(120)


# ─── TKINTER PAGE ───────────────────────────────────────────────────────────────
x = IntVar()
main = Tk()
Entry(main , textvariable  = x).pack()
Button(main , text = "press",  command = press).pack()
Button(main  , text = "circle", command = circle , bg = ("#B39DDB")).pack()
Button(main  , text = "square", command = square, bg = ("#FFE082")).pack()
Button(main  , text = "rectangle", command = rectangle, bg = ("#18FFFF")).pack()

mainloop()