from tkinter import Tk , Entry , Button , Label , StringVar
main = Tk()



main.geometry("340x220")

def press ():
    sv_out.set("poulstar")


sv_out = StringVar()
Label(main , textvariable = sv_out).pack()


Entry(main , bg= "#26C6DA" ) .pack()

Button(main , text = "press" , command = press , bg= "#3949AB").pack()

main.mainloop()

