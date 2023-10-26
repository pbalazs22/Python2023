import random
toto=list(range(1, 14))
random.shuffle(toto)
totosz=toto[:3]
totósz= [random.randrange(1, 4) for totósz in range(13)]
for i in range(len(totósz)):
    pass
    if totósz[i]==3:
        totósz[i]="x"
menu=["1: ötös lottó","2 hatos lottó","3 Skandináv","4 Totó","0 kilépés"]
while True:
    for minden in menu:
        pass
   

    x=input("\nMelyik szerencsejáték számai legyenek legenerálva? \n1 ötös lottó \n2 hatos lottó \n3 Skandináv \n4 Totó \n0 kilépés\n"  )
    print(x)
    if x=="1":
        ötös=list(range(1, 91))
        random.shuffle(ötös)
        ötössz=ötös[:5]
        otoski = "Az ötös lottó számaira ezek a tippeim: \n1.szám: {} \n2.szám: {} \n3.szám: {} \n4.szám: {} \n5.szám: {}"
        ötössz.sort()
        print(otoski.format(ötössz[0],ötössz[1],ötössz[2],ötössz[3],ötössz[4]))
        
    if x=="2":
        hatos=list(range(1, 46))
        random.shuffle(hatos)
        hatossz=hatos[:6]
        hatoski = "A hatos lottó számaira ezek a tippeim: \n1.szám: {} \n2.szám: {} \n3.szám: {} \n4.szám: {} \n5.szám: {} \n6.szám: {}"
        hatossz.sort()
        print(hatossz)
    if x=="3":
        skandinav=list(range(1, 36))
        random.shuffle(skandinav)
        skandinavsz=skandinav[:7]
        skandinavsz.sort()
        print(skandinavsz)
    if x=="4":
        print(totósz)
    if x=="0":
        exit()
