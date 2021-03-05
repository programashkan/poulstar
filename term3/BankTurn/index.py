

#date
#time
#your turn number
#Queue

from tkinter import *
import jdatetime


# ─── GLOBAL VARIABLE ────────────────────────────────────────────────────────────
counter = 0
list_number = []



# ─── FUNCTION ───────────────────────────────────────────────────────────────────



def set_number():
    global counter
    counter += 1
    list_number.append(counter)
    return list_number







# ─── BANK PAGE ──────────────────────────────────────────────────────────────────

bank = Tk()
bank.geometry("640x480")

Button(bank, text="Oprator 1").grid(row=0, column=0)
Button(bank, text="Oprator 2").grid(row=0, column=1)
Button(bank, text="Oprator 3").grid(row=0, column=2)

Button(bank, text="Next Costumer...", command=set_number).grid(row=1, column=1)


# ─── RECEPT PAGE ────────────────────────────────────────────────────────────────



recept = Toplevel()
recept.geometry("640x480")

Label(recept, text=jdatetime.datetime.now().strftime("%a, %d %b %Y")).grid(row=0, column=0)
Label(recept, text=jdatetime.datetime.now().strftime("%H:%M:%S")).grid(row=1, column=0)

number = set_number()
print(number)

# Label(recept, text=str(number)).grid(row=2, column=0)




bank.mainloop()




