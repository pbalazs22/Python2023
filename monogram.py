import transzformaciok
from tkinter import *

# Create an instance of tkinter frame or window
win=Tk()

# Set the size of the tkinter window
win.geometry("700x550")

# Create a canvas widget
canvas=Canvas(win, width=500, height=300, background="#00ffff")
canvas.pack(fill=BOTH,expand=1)

betuk=[
        [0,0,0,100,60,100,80,80,80,70,60,50,80,30,80,20,60,0,0,0],#B
        [120,100,150,0,180,100],#A
        [100,50,200,50],#A
        [240,0,240,100,300,100],#L
        [340,100,370,0,400,100],#Á
        [320,50,420,50],#Á
        [390,-20,380,3],#Á
        [440,0,500,0,440,100,500,100],#Z
        [540,100,560,85,565,55,540,20,565,0]
    ]

#konfigurálás
meret=1
meret2=1
fok=0
dX=10
dY=10

for i in range(len(betuk)):
    betuk[i]=transzformaciok.nagyit(betuk[i],meret,meret2)

xy=transzformaciok.kozepPont(betuk)

for i in range(len(betuk)):
    betuk[i]=transzformaciok.forgat(betuk[i],fok,xy[0],xy[1])

#teto=nagyit(teto,meret,meret2)
#fal=nagyit(fal,meret,meret2)

for i in range(len(betuk)):
    betuk[i]=transzformaciok.eltol(betuk[i],dX,dY)        


for i in range(len(betuk)):
    canvas.create_line(betuk[i],fill="brown",width=3)



win.mainloop()