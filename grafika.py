# Import the required libraries
from tkinter import *

def haziko(canvas):
    teto=[10,10,20,10,15,5,10,10]
    fal=[10,10,20,10,20,20,10,20,10,10]
    canvas.create_line(teto,fill="brown",width=5)
    canvas.create_line(fal,fill="yellow",width=5)



# Create an instance of tkinter frame or window
win=Tk()

# Set the size of the tkinter window
win.geometry("700x350")

# Create a canvas widget
canvas=Canvas(win, width=500, height=300, background="#bbbbbb")
canvas.pack(fill=BOTH,expand=1)

# Add a line in canvas widget
#canvas.create_line(0,0,200,100, fill="green", width=5)

#canvas.create_line(0,0,200,100, fill="green", width=5)

for i in range(70):
    canvas.create_line(10*i,0,10*i,30, fill="green", width=5)

#canvas.create_line(100,100,500,100,fill="blue",width=1)
#canvas.create_line(500,100,500,500,fill="blue",width=1)
#canvas.create_line(500,500,100,500,fill="blue",width=1)
#canvas.create_line(100,500,100,100,fill="blue",width=1)

lista=[100,100,500,100,500,500,100,500,100,100]
canvas.create_line(lista,fill="blue",width=1)

canvas.create_line(100,100,500,100,fill="blue",width=1)

egyHaromszog=[250,250,350,250]
canvas.create_line(egyHaromszog,fill="red",width=1)

haziko(canvas)

win.mainloop()