from tkinter import *
main = Tk()
canvas_width = 500
canvas_height = 150

def paint( event ):
   
   python_color = ("#")
   x1, y1 = ( event.xd32f2f - 3 ), ( event.y - 3 )
   x2, y2 = ( event.x + 3 ), ( event.y + 3 )
   w.create_oval( x1, y1, x2, y2, fill = python_color )

master = Tk()
master.title( "Painting using Ovals" )
w = Canvas(master, 
           width=canvas_width, 
           height=canvas_height)
w.pack(expand = YES, fill = BOTH)
w.bind( "<B1-Motion>", paint )

message = Label( master, text = "Press and Drag the mouse to draw" )
message.pack( side = BOTTOM )
w.mainloop()
