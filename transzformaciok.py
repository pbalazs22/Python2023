import math

def eltol(pontok,dX,dY):
    for i in range(0,len(pontok),2):
        pontok[i]+=dX
    for i in range(1,len(pontok),2):
        pontok[i]+=dY
    
    return pontok

def nagyit(pontok,meret,meret2=-1):
    #x koordináták
    for i in range(0,len(pontok),2):
        pontok[i]*=meret
    #y koordináták
    if meret2==-1:
        for i in range(1,len(pontok),2):
            pontok[i]*=meret
    else:
        for i in range(1,len(pontok),2):
            pontok[i]*=meret2

    return pontok

def forgat(pontok,fok,oX="",oY=""):
#x0 = cos αx − sin αy
#y0 = sin αx + cos αy
    if oX=="" and oY=="":
        kp=kozepPont([pontok])
        oX=kp[0]
        oY=kp[1]

    #eltolás origóba
    pontok2=eltol(pontok,-oX,-oY)
    #forgatás origó körül
    pontok3=[]
    for i in range(0,len(pontok2),2):
        x=pontok2[i]
        y=pontok2[i+1]
        pontok3.append(math.cos(math.radians(fok))*x - math.sin(math.radians(fok))*y)
        pontok3.append(math.sin(math.radians(fok))*x + math.cos(math.radians(fok))*y)

    #visszatolás a helyére
    pontok3=eltol(pontok3,oX,oY)
    return pontok3

def kozepPont(pontok):
    x_ek=[]
    y_ok=[]
    for e in pontok:
        for i in range(0,len(e),2):
            x_ek.append(e[i])
            y_ok.append(e[i+1])

    #súlypont
    x=sum(x_ek)/len(x_ek)
    y=sum(y_ok)/len(y_ok)

    return [x,y]
            

if __name__ =="__main__":
    print("rendesen elindítva")
else:
    print("modulként betöltve")