import random

toto = list(range(1, 14))
random.shuffle(toto)
totosz = toto[:3]
totoki = "A Totó számaira ezek a tippeim:\n1.szám: {}\n2.szám: {}\n3.szám: {}\n4.szám: {}\n5.szám: {}\n6.szám: {}\n7.szám: {}\n8.szám: {}\n9.szám: {}\n10.szám: {}\n11.szám: {}\n12.szám: {}\n13.szám: {}"
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
        print(hatoski.format(hatossz[0],hatossz[1],hatossz[2],hatossz[3],hatossz[4],hatossz[5]))
    if x=="3":
        skandinav=list(range(1, 36))
        random.shuffle(skandinav)
        skandinavsz=skandinav[:7]
        skandinavki="A Skandináv számaira ezek a tippeim: \n1.szám: {} \n2.szám: {} \n3.szám: {} \n4.szám: {} \n5.szám: {} \n6.szám: {} \n7.szám: {}"
        skandinavsz.sort()
        print(skandinavki.format(skandinavsz[0],skandinavsz[1],skandinavsz[2],skandinavsz[3],skandinavsz[4],skandinavsz[5],skandinavsz[6]))
    if x=="4":
        toto = list(range(1, 14))
        random.shuffle(toto)
        totosz = toto[:3]
        totósz = [random.randrange(1, 4) for _ in range(13)]
        for i in range(len(totósz)):
            if totósz[i] == 3:
                totósz[i] = "x"
        print(totoki.format(totósz[0], totósz[1], totósz[2], totósz[3], totósz[4], totósz[5], totósz[6], totósz[7], totósz[8], totósz[9], totósz[10], totósz[11], totósz[12]))
    if x=="0":
        exit()
