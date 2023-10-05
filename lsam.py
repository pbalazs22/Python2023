

hosszúság=["mm","cm","dm","m","km"]
hosszváltás=[10,10,10,1000,1]

terület=["mm2","cm2","dm2","m2","km2"]
terváltás=[100,100,100,1000000,1]

repeat="igen"
while(repeat=="igen"):
    #szam bekérés
    #szam ellenörzés
    rossz=True
    while rossz:
        try:
            szam=float(input("írj egy számot:"))
            rossz=False
        except:
            print("ez nem jó!")






    #mértékegység bekérés


    rossz=True
    while rossz:
        mertekEgyseg=input("Kérem a mértékegységet:")
        #mértékegység ellenörzés, típus kiderítés
        if mertekEgyseg in hosszúság:
            rossz=False
        else:
            print("ismeretlen mertekegyseg: "+mertekEgyseg)

    #mértékegység2 bekérés

    rossz=True
    while rossz:
        mertekEgyseg2=input("Kérem a mértékegységet:")
        #mértékegység2 ellenörzés, az 1. típusból
        if mertekEgyseg2 in hosszúság:
            rossz=False
        else:
            print("ismeretlen mertekegyseg: "+mertekEgyseg2)



    #kiszámítás
    me1Index = hosszúság.index(mertekEgyseg)
    me2Index = hosszúság.index(mertekEgyseg2)
    #print(me1Index, me2Index)

    #print(hosszváltás[me1Index:me2Index])
    if me1Index<me2Index:
        szorzo=1
        for valto in (hosszváltás[me1Index:me2Index]):
            szorzo = szorzo * valto

        szam=szam/szorzo
    else:
        szorzo=1
        for valto in (hosszváltás[me2Index:me1Index]):
            szorzo = szorzo * valto
        szam=szam*szorzo
    #kiírás


    print(szam,mertekEgyseg2)
    #újra?

    repeat=input("Újra? (igen/nem):")

