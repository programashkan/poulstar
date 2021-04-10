<<<<<<< HEAD


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
=======
# ─── CLASS ──────────────────────────────────────────────────────────────────────

from tkinter import *
import jdatetime
# ─── PACKAGES ───────────────────────────────────────────────────────────────────




# ─── VARIABLE ───────────────────────────────────────────────────────────────────

counter = 0
list_number = []

# ─── RECEPT PAGE ────────────────────────────────────────────────────────────────
def get_turns():
    global counter
    counter += 1
    list_number.append(counter)
    recept = Toplevel()
    recept.geometry("640x480")
    Label(recept , text = jdatetime.datetime.now().strftime("%a  , %d , %b , %y" )).grid(row=1 , column = 0)
    Label(recept , text = jdatetime.datetime.now().strftime(" %H : %M : %S" )).grid(row=2 , column = 0)
    iv_counter = IntVar()
    iv_counter.set(counter)
    Label(recept , textvariable = iv_counter).grid(row=3 , column = 0)
    iv_list_number = IntVar()
    iv_list_number.set(len(list_number))
    Label(recept , textvariable = iv_list_number).grid(row=4 , column = 0)

# ─── OPERATOR ───────────────────────────────────────────────────────────────────

def operator():
    print(list_number.pop(0))


# ─── BANK PAGE ──────────────────────────────────────────────────────────────────
bank = Tk()
bank.geometry("320x340")
Button(bank, text = "coperator1", command  = operator).grid(row = 0 , column= 1)
Button(bank, text = "coperator2", command  = operator).grid(row = 0 , column= 2)
Button(bank, text = "coperator3", command  = operator).grid(row = 0 , column= 3)
Button(bank, text = "click for get turn" , command = get_turns).grid(row = 1 , column= 2)








>>>>>>> 0920b6b (99/12/23)




bank.mainloop()



<<<<<<< HEAD

=======
>>>>>>> 0920b6b (99/12/23)
