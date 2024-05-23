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
        [540,100,560,85,565,55,540,20,565,0],
        [200,200,300,200,300,300,200,300,200,200],
        [220,220,280,220,280,280,220,280,220,220],
        
        [400,200,500,200,500,300,400,300,400,200],
        [420,220,480,220,480,280,420,280,420,220],

    ]
szinek=["red","black","green","Blue","white","orange","Purple","red","blue","orange","white","green","purple"]
#konfigurálás
meret=1
meret2=1
fok=0
dX=10
dY=10

for i in range(len(betuk)):
    betuk[i]=transzformaciok.nagyit(betuk[i],meret,meret2)

xy=transzformaciok.kozepPont(betuk)


#teto=nagyit(teto,meret,meret2)
#fal=nagyit(fal,meret,meret2)

for i in range(len(betuk)):
    betuk[i]=transzformaciok.eltol(betuk[i],dX,dY)        

for i in range(len(betuk)):
        betuk[i]=transzformaciok.forgat(betuk[i],fok,xy[0],xy[1])

for i in range(len(betuk)):
    canvas.create_polygon(betuk[i],fill=szinek[i],width=3)

arnyek=[]

for i in range(len(betuk)):
    arnyek.append(transzformaciok.forgat(betuk[i],0,0,0))

for i in range(len(arnyek)):
    arnyek[i]=transzformaciok.eltol(arnyek[i],5,5) 


for i in range(len(arnyek)):
    arnyek[i]=transzformaciok.eltol(arnyek[i],5,5) 


fok=0.01
novekedes=1.001
szamol=0
irany=1
while True:
    szamol+=irany
    canvas.delete("all")
    
    if szamol  >300:
        irany*=-1
        novekedes=1/novekedes
    if szamol<0:
        irany*=-1
        novekedes=1/novekedes
        
    
    
    for i in range(len(arnyek)):
        arnyek[i]=transzformaciok.forgat(arnyek[i],fok,xy[0],xy[1])
        arnyek[i]=transzformaciok.nagyit(arnyek[i],novekedes,novekedes)
    for i in range(len(arnyek)):
        canvas.create_polygon(arnyek[i],fill="grey")
    for i in range(len(betuk)):
        betuk[i]=transzformaciok.forgat(betuk[i],fok,xy[0],xy[1])
    for i in range(len(betuk)):
        canvas.create_polygon(betuk[i],fill=szinek[i],width=3)
    
  


        win.update()
        #win.mainloop()