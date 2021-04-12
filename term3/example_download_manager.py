from tkinter import *
from tkinter import messagebox, filedialog
import os
from urllib.request import urlopen, HTTPError, URLError
import _thread



main = Tk()
main.geometry("450x400")
main.title("download manager")
main.configure(bg = ("#9FA8DA"))
### ─── FILE ─────────────────────────────────────────────────────────────────

url = StringVar()
###
file_name = StringVar()
###
download_progress = StringVar()
###
download_per = StringVar()
###
fln = ''
###
file_size = ''


### ─── FUANCTIONS ─────────────────────────────────────────────────────────────────
def exit_btn():
    if messagebox.askyesno("Exit program ?", "Are you sure you want to exit the program?") == False :
        return False
    
    exit()


def start_download():
    global fln
    fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title = "save file", filetypes=(("espace file", "*.png"), ("All Files", "*.*") ))
    file_name.set(os.path.basename(fln))
    _thread.start_new_thread(init_download, ())

def init_download():
    global file_size
    furl = url.get()
    target = urlopen(furl)
    meta = target.info()
    file_size = float(meta['Content-Length'])
    file_size_mb = round(file_size / 1024 / 1024, 2)
    downloaded = 0
    chunks = 1024 * 5
    with open(fln, "wb") as f :
        while True:
            parts = target.read(chunks)
            if not parts:
                messagebox.showinfo("Download Complete", "your Download Has Been Completed Successfully.")
                break
            downloaded += chunks
            perc = round(((downloaded / file_size) * 100),2)
            if perc > 100:
                perc = 100
            download_progress.set(str((round(downloaded / 1024 / 1024), 2))+" MB / " +str(file_size_mb) + "MB")
            download_per.set(str(perc)+"%")
            f.write(parts)
    f.close()
            


        
# ─── BOX DOWNLOAD ───────────────────────────────────────────────────────────────

box1= LabelFrame(main, text = "file URL", bg = ("#FFF176"))
box1.pack(fill = "both", expand = "yes", pady = 10, padx = 10)
###
lbl01 = Label(box1, text = "download URL : ", bg = ("#FFF176"))
lbl01.grid(row = 0, column = 0 , pady = 10, padx = 10)
###
ent = Entry(box1, textvariable = url)
ent.grid(row = 0 , column = 1, pady = 5, padx = 10)
###
btn01 = Button(box1, command = start_download, text = "download", bg = ("black"), fg = ("white"))
btn01.grid(row = 1, column = 1 , pady = 10, padx = 10)


# ─── BOX INFORMATION ────────────────────────────────────────────────────────────

box2 = LabelFrame(main, text = "Download information", bg = ("#18FFFF"))
box2.pack(fill = "both", expand = "yes", pady = 10, padx = 10)

lbl02 = Label(box2, text = "File : ", bg = ("#18FFFF"))
lbl02.grid(row = 0, column = 0 , pady = 10, padx = 10)
lbl03 = Label(box2, textvariable = file_name, bg = ("#18FFFF"))
lbl03.grid(row = 0, column = 1 , pady = 10, padx = 10)
###
lbl04 = Label(box2, text = "Download progress : ", bg = ("#18FFFF"))
lbl04.grid(row = 1, column = 0 , pady = 10, padx = 10)
lbl05 = Label(box2, textvariable = download_progress, bg = ("#18FFFF"))
lbl05.grid(row = 1, column = 1 , pady = 10, padx = 10)
###
lbl06 = Label(box2, text = "Download percentage : ", bg = ("#18FFFF"))
lbl06.grid(row = 2, column = 0 , pady = 10, padx = 10)
lbl07 = Label(box2, textvariable = download_per, bg = ("#18FFFF"))
lbl07.grid(row = 2, column = 1 , pady = 10, padx = 10)
###
Button(box2, text = "Exit downloader", command = exit_btn, bg = ("black"), fg = ("white")).grid(row = 3, column = 0 , pady = 10, padx = 10, )

main.mainloop()