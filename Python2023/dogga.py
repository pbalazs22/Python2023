import random

def parosDarab(lista):
    darab=[]
    for e in lista:
        if e%2==0:
            darab.append(e)
            db+=1
    return len(darab)

szamok=[]
for _ in range(500):
    szamok.append(random.randrange(10000,100000))

print("Ennyi páros van a listában: {}".format(parosDarab(szamok)))

osszeg=0
for e in szamok:
    if e%2==1:
        osszeg+=e

print("A páratlan számok összege {}".format(osszeg))
      
paratlanok=[]
for e in szamok:
    if e%==1:
paratlanok.append(e)



