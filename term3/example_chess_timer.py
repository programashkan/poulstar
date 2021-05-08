from tkinter import *
from time import sleep
from threading import Thread


def start():
    global left
    while True:
        if left:
            sv_time02.set(sv_time02.get() -1)




        else:
            sv_time01.set(sv_time01.get() -1)
                    
        sleep(1)



def thr_s():
    thr_start = Thread(target = start , args=())
    thr_start.start()


def stop_01():
    global left
    left = True


def stop_02():
    global left
    left = False


main = Tk()

left = True

sv_time01 = IntVar()
sv_time01.set(20)
sv_time02 = IntVar()
sv_time02.set(20)


Label(main, textvariable =  sv_time01 ).grid(row = 0, column= 0)
Label(main, textvariable =  sv_time02 ).grid(row = 0, column= 1)

Button(main , text = "stop", command = stop_01).grid(row = 1, column= 0)
Button(main , text = "stop", command = stop_02).grid(row = 1, column= 1)
Button(main , text = "Start", command = thr_s).grid(row = 2, column= 0)
main.mainloop()
