from tkinter import Tk , Toplevel , Button , Entry
def press():
    root = Toplevel()
    Entry(root , bg = ("#4DD0E1")).pack()


main = Tk()
Button(main , text = "hello world" , command = press).pack()



main.mainloop()
