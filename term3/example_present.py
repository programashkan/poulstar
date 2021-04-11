import wget
from tkinter import *
main = Tk()
t = Toplevel()
sv_geturl = StringVar()
def download():
    get_url = sv_geturl.get()
    wget.download(get_url)
    
Label(main, text = "pls put your url").pack()
Entry(main, textvariable = sv_geturl).pack()

Button(main, command = download , text = "press to download", bg = ("#FFEB3B")).pack()

mainloop()
wget.callback_progress()




#url = 'http://www.futurecrew.com/skaven/song_files/mp3/razorback.mp3'
#filename = wget.download(url)
