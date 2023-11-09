def menu(lista):
    for i,szoveg in enumerate(lista):
        print("{}: {}".format(i+1,szoveg))

    valasz=-1
    while (valasz<1 or valasz>len(lista)) and valasz!=999:
        try:
            valasz=int(input("Válassz: "))
        except:
            pass
    return valasz-1


lista=["előre","hátra","jobbra","balra"]

#valasztott=menu(lista)
#print(valasztott,lista[valasztott])

#valasztott=menu(lista)
#print(valasztott,lista[valasztott])

tortenet=[
    [
        1,  #történetszál sorszáma
        "Reggel felkeltem.",#történetszál
        ["fogmosás","reggeli", "öltözés"],#választható cselekvések
        [2,3,4]#cselekvés sorszáma, hova ugorjon
    ],
    [
        2,
        "Megmostam a fogam, mert még van!",
        ["fogmosás","reggeli", "öltözés"],#választható cselekvések
        [2,3,4]#cselekvés sorszáma, hova ugorjon
    ]
]
szalId=1
while True:
    tempLista=[]
    for elem in tortenet:
        tempLista.append(elem[0])

    keresettIndex=tempLista.index(szalId)
    print(tortenet[keresettIndex][1])
    valasztott=menu(tortenet[keresettIndex][2])

    szalId=tortenet[keresettIndex][3][valasztott]
    if valasztott==999:
        break
