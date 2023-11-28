def legkonnyebb():
    legkisebb=tomegek[0]
    for t in tomegek:
        if legkisebb>t:
            legkisebb=t

    return legkisebb


#egy lista amibe 10 állat van, készitsünk egy programot ami bekéri ezeknek az állatoknak a tömegét, ezt is menztse le , aztán egy függvény ami megkeresi a legkisseb tömegü állatot és visszaadja az adatait 

allatok=["majom","kenguru","csincsilla","elefánt","vaddisznó","kutya","ló","macska","cápa","gepárd"]

tomegek=[]
    
tomegek=[12,2,3,4,5,6,7,8,9,10]

#for allat in allatok:
#   tomegek.append(float(input("Milyen nehéz a "+allat+"(kg):")))


print(legkonnyebb())

if legkonnyebb() in tomegek:
    id=tomegek.index(legkonnyebb())
    print(allatok[id])

nehezek=[]

for i in range(len(tomegek)):
    pass
