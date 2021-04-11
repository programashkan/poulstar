from tkinter import *
from tkinter import mainloop, filedialog
import os

main = Tk()
main.geometry("450x400")
main.title("download manager")
# ─── FUANCTIONS ─────────────────────────────────────────────────────────────────

def start_download():
    pass
# ─── STRINGVARS ─────────────────────────────────────────────────────────────────

url = StringVar()




# ─── BOX DOWNLOAD ───────────────────────────────────────────────────────────────


box1 = LabelFrame(main, text = "file URL")
box1.pack(fill = "both", expand = "yes", pady = 10, padx = 10)

lbl01 = Label(box1, text = "download URL : ")
lbl01.grid(row = 0, column = 0 , pady = 10, padx = 10)

ent = Entry(box1, textvariable = url)
ent.grid(row = 0 , column = 1, pady = 5, padx = 10)

btn01 = Button(box1, command = start_download, text = "download")
btn01.grid(row = 1, column = 1 , pady = 10, padx = 10)

# ─── BOX INFORMATION ────────────────────────────────────────────────────────────

box2 = LabelFrame(main, text = "download information")
box2.pack(fill = "both", expand = "yes", pady = 10, padx = 10)

#

main.mainloop()