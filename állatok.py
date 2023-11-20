def legkonnyebb():
    print(tomegek)

    pass




#egy lista amibe 10 állat van, készitsünk egy programot ami bekéri ezeknek az állatoknak a tömegét, ezt is menztse le , aztán egy függvény ami megkeresi a legkisseb tömegü állatot és visszaadja az adatait 

allatok=["majom","kenguru","csincsilla","elefánt","vaddisznó","kutya","ló","macska","cápa","gepárd"]

tomegek=[]

for allat in allatok:
    tomegek.append(float(input("Milyen nehéz a "+allat+"(kg):")))


legkonnyebb()
