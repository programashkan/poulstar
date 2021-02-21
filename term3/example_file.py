from tkinter import Tk , Label , Entry , StringVar , Button
main = Tk()
def press ():
    sv01 = sv_get01.get()\
    file = open("text.txt" , "w")
    file.write(sv01)
    file.close()


Label(main , text = "write your name |").pack()

sv_get01 = StringVar()
Entry(main , textvariable = sv_get01).pack()
Button(main , command = press , text = "press").pack()
main.mainloop()