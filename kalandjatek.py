def menu(lista):
    for i,szoveg in enumerate(lista):
        print("{}: {}".format(i+1,szoveg))

    valasz=-1
    while (valasz<1 or valasz>len(lista)) and valasz!=999:
        try:
            valasz=int(input("Válasz: "))
        except:
            pass
    return valasz-1


#valasztott=menu(lista)
#print(valasztott,lista[valasztott])

#valasztott=menu(lista)
#print(valasztott,lista[valasztott])

nyelvek=["Magyar","English"]
nyelvId=menu(nyelvek)

if nyelvId==0:
    import tortenetmagyar as t
elif nyelvId==1:
    import tortenetangol as t

szalId=1
while True:
    tempLista=[]
    for elem in t.tortenet:
        tempLista.append(elem[0])

    keresettIndex=tempLista.index(szalId)
    print(t.tortenet[keresettIndex][1])
    valasztott=menu(t.tortenet[keresettIndex][2])

    szalId=t.tortenet[keresettIndex][3][valasztott]
    if valasztott==999:
        break

    keresettIndex=tempLista.index(szalId)

    print(t.tortenet[keresettIndex][1])
    valasztott=menu(t.tortenet[keresettIndex][2])

    szalId=t.tortenet[keresettIndex][3][valasztott]
    if valasztott==999:
        break





