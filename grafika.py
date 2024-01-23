# Import the required libraries
from tkinter import *
import math
def haziko(canvas,dX,dY,meret,meret2=-1,fok=36):
    haz=[
        [10,10,20,10,15,5,10,10],#teto
        [10,10,20,10,20,20,10,20,10,10],#fal
        [13,20,13,15,17,15,17,20]#ajto
    ]
    #teto=[10,10,20,10,15,5,10,10]
    #fal=[10,10,20,10,20,20,10,20,10,10]
    #ajto=[13,20,13,15,17,15,17,20]

    for i in range(len(haz)):
        haz[i]=nagyit(haz[i],meret,meret2)

    for i in range(len(haz)):
        haz[i]=forgat(haz[i],fok)

    #teto=nagyit(teto,meret,meret2)
    #fal=nagyit(fal,meret,meret2)    
    
    for i in range (len(haz)):
        haz[i]=eltol(haz[i],dX,dY)
    
    
    #teto=eltol(teto,dX,dY)
    #fal=eltol(fal,dX,dY)
        
    for i in range(len(haz)):
        canvas.create_line(haz[i],fill="brown",width=3)
    

def eltol(pontok,dX,dY):
    for i in range(0,len(pontok),2):
        pontok[i]+=dX
    for i in range(1,len(pontok),2):
        pontok[i]+=dY




    return pontok

def forgat(pontok,fok,oX="",oY=""):
     #x kordinata
    if oX=="" and oY=="":
        kp=kozéppont([pontok])
        oX=kp[0]
        oY=kp[1]


    #eltolás origoba
    pontok2=eltol(pontok,-oX,-oY)
    #forgatas origo korul
    pontok3=[]
    for i in range(0,len(pontok),2):
        x=pontok2[i]
        y=pontok2[i+1]
        pontok3.append(math.cos(math.radians(fok))*x - math.sin(math.radians(fok))*y)
        pontok3.append(math.sin(math.radians(fok))*x + math.sin(math.radians(fok))*y)         
    
    #visszatolás 
    pontok3=eltol(pontok3,oX,oY)
    
    return pontok3

def nagyit(pontok,meret,meret2=-1):

    for i in range(0,len(pontok),2):
        pontok[i]*=meret

    if meret2==-1:   
        for i in range(1,len(pontok),2):
            pontok[i]*=meret
    else: 
            for i in range(1,len(pontok),2):
                pontok[i]*=meret2

    return pontok

def kozéppont(pontok):
    x_ek=[]
    y_ok=[]
    for e in pontok:
        for i in range(0,len(e),2):
            x_ek.append(e[i])
            y_ok.append(e[i+1])
    x=sum(x_ek)/len(x_ek)
    y=sum(y_ok)/len(y_ok)

    return[x,y]
# Create an instance of tkinter frame or window
win=Tk()

# Set the size of the tkinter window
win.geometry("700x350")

# Create a canvas widget
canvas=Canvas(win, width=500, height=300, background="#bbbbbb")
canvas.pack(fill=BOTH,expand=1)

haziko(canvas,200,200,5)

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



haziko(canvas,200,200,5)
haziko(canvas,100,100,6, fok=20)


win.mainloop()