import random
ötös=list(range(1, 91))
random.shuffle(ötös)
ötössz=ötös[:5]

hatos=list(range(1, 46))
random.shuffle(hatos)
hatossz=hatos[:6]

skandinav=list(range(1, 36))
random.shuffle(skandinav)
skandinavsz=skandinav[:7]

toto=list(range(1, 14))
random.shuffle(toto)
totosz=toto[:3]

totósz= [random.randrange(1, 4) for totósz in range(13)]

menu=["1: ötös lottó","2 hatos lottó","3 Skandináv","4 Totó","0 kilépés"]
while True:
    for minden in menu:
        pass
    x=input("Melyik szerencsejáték számai legyenek legenerálva? \n1 ötös lottó \n2 hatos lottó \n3 Skandináv \n4 Totó \n0 kilépés\n"  )
    print(x)
    
    if x=="1":
        print(hatossz)
    if x=="2":
        print(hatossz)
    if x=="3":
        print(skandinavsz)
    if x=="4":
        print(totósz)
    if x=="0":
        exit()
