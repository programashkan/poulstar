from tkinter import Tk , Entry , Label , Button , StringVar
main = Tk()
main.geometry("250x500")
main.configure(bg = "#BA68C8")
def cale ():
    number01 = int(sv_number01.get())
    number02 = int(sv_number01.get())
    sum = number01 + number02
    min = number02 - number01
    div = number01 / number02
    mul = number01 * number02
    pow = number01 ** number02
    mod = number01 % number02

    sv_out.set(
        "sum is:" + str(sum )+ " \n"
        "min is:" + str(min)+ "\n"
        "div is: " + str(div) + "\n"
        "mul is :" + str (mul) +"\n"
        "pow is :" + str(pow ) + "\n"
        "mod is :" + str (mod) + "\n")

# entry
sv_number01 = StringVar()
Entry(main ,textvariable = sv_number01 , bg= ("#90CAF9") ).pack() 



sv_number02 = StringVar()
Entry(main ,textvariable = sv_number02, bg= ("#9FA8DA") ).pack() 

#bottoms
Button(main , text = "" , command = cale , bg = ("#C2185B")).pack()
Button(main, text="Exit",fg = ("#BA68C8"),  command=main.destroy).pack()
sv_out = StringVar()
Label(main , textvariable =sv_out , bg = ("#B3E5FC")).pack()




main.mainloop()