i=1
szó=input("{}.szó:".format("1"))
szolanc=[]
szolanc.append(szó)
elozoszo=szó[-1]

while True:
    szó=input("{}.szó:".format(i+1))
    if len(szó) != 6:
        print("A karakter száma téves")
        break

    if szó[0] != elozoszo:
        print("Nem illeszkedett!")
        break

    szolanc.append(szó)
    i+=1

if len(szolanc) <= 2:
    print("Szint: kezdő")
elif len(szolanc) > 2 and len(szolanc) < 6:
    print("Szint: közepes")
else:
    print("Szint: Magas")


print("Helyes lépések száma:{}".format(len(szolanc)))

    