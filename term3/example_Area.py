from tkinter import Tk , Button , Label , Entry , StringVar
main = Tk()
main.configure(bg = ("#ffcdd2"))
Label(main , text = "pls enter what area you want -->" ,  fg = ("#81D4FA")).grid(row =0, column =0)
main.geometry("600x200")
def press():
    global area01
    area01 = sv_area.get()
    

def area ():
    number01 = int (sv_number01.get())
    number02 = int(sv_number02.get())
    if area01 == "triangle":
        triangle01 = number01 * number02 / 2
        sv_out02.set("your area is:    " + str(triangle01))
    if area01 == "square":
        square = number01 * number02
        sv_out02.set("your area is:    " + str(square))
    if area01 == "Rectangle":
        mos = number02 * number01
        sv_out02.set("your area is:    " + str(mos))
    if area01 == "circle":
        cir = number02 * number01 * 3.14
        sv_out02.set("your area is:    " + str(cir))

sv_area = StringVar()
Entry(main , textvariable = sv_area , bg = ("#E0E0E0")).grid(row =0, column =1)
Button(main , text = "press to countinuo" , command = press , bg = ("#C5CAE9")).grid(row =1, column =1)
Label(main , text = "type of area u can pick : " , fg = ("#80CBC4")).grid(row =0, column =2)
Label(main , text = "triangle " , fg = ("#D81B60")).grid(row =1, column =2)
Label(main , text = "square " , fg = ("#D81B60")).grid(row =2, column =2)
Label(main , text = " Rectangle" ,fg = ("#D81B60") ).grid(row =3, column =2)
Label(main , text = " circle", fg = ("#D81B60") ).grid(row =4, column =2)
Label(main , text = " pls write this word well like this example :-) " , fg = ("#3F51B5") ).grid(row =5, column =2)
Label(main , text = " pls enter  Radius for circle two time :)" , fg = ("#3F51B5") ).grid(row =6, column =2)
sv_number01 = StringVar()
Entry(main ,textvariable = sv_number01 , bg = ("#84FFFF") ).grid(row =2, column =1)

sv_number02 = StringVar()
Entry(main ,textvariable = sv_number02  , bg = ("#80D8FF")).grid(row =3, column =1)



Label(main,  text = "length  , ghaede -->" , fg = "#FFAB91" ).grid(row =2, column =0)
Label(main,  text = "Width  , Height -->" , fg = "#FF8A65").grid(row =3, column =0)

Button(main , text = "click to Computing" , command = area , bg = ("#9575CD") ).grid(row =4, column =1)



sv_out = StringVar()

Label(main , textvariable = sv_out , fg = "#80CBC4" ).grid(row =5, column =1)

sv_out02 = StringVar()
Label(main , textvariable = sv_out02 , fg = ("#212121")).grid(row =6, column =1)



main.mainloop()















main.mainloop()