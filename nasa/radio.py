import radioModul

def megfejtes(napiuzenetek):
    vissza=napiuzenetek[0].szoveg

    for i in range(len(vissza)):
        if vissza[i]=="#":
            uj=betuKeres(napiuzenetek,i)
            vissza=vissza[:i]+uj+vissza[i+1:]
    return vissza




def betuKeres(napiUzenetek,sorszam):
    for egyUzenet in napiUzenetek:
        if egyUzenet.szoveg[sorszam] !="#":
            return egyUzenet.szoveg[sorszam]
        
    return "#"
def szame(szo):
    #valasz:=igaz
    valasz=True
    #Ciklus i:=1
    for i in range(len(szo)):
        if szo[i]<"0" or szo[i] > "9":
            valasz=False

    return valasz

uzenetek=[]
f=open("veetel.txt")
for sor in f:
    sor2=f.readline()
    uzenetek.append(radioModul.uzenet(sor,sor2))

f.close()

print("2. feladat")
print("Az első üzenet rögzítője: {}".format(uzenetek[0].amator))
print("Az utolsó üzenet rögzítője: {}".format(uzenetek[-1].amator))


print("3. feladat")
for egyUzenet in uzenetek:
    if egyUzenet.farkasVan():
        print("{}. nap {}. rádióamatőr".format(egyUzenet.nap,egyUzenet.amator))


napok=[]
for NapSzam in range(1,12):
    tempNap=[]
    for egyUzenet in uzenetek:
        if egyUzenet.nap==NapSzam:
            tempNap.append(egyUzenet)

    napok.append(tempNap)

print("4.feladat")
for NapSzam in range(11):
    print("{}. nap: {} rádióamatőr".format(NapSzam+1,len(napok[NapSzam])))

f=open("adaas.txt","w")
for egyNap in napok:
    f.write(megfejtes(egyNap))

f.close()


print(megfejtes(napok[0]))

print("7. feladat")
NapSzam=int(input("Adja meg a nap sorszámát!"))
amatorSzam=int(input("Adja meg a radióamatör sorszámát!"))

for egyUzenet in uzenetek:
    if egyUzenet.nap==NapSzam and egyUzenet.amator==amatorSzam:
        print(egyUzenet.szoveg)
        ertek=egyUzenet.szoveg.split(" ")[0].split("/")
        if len(ertek)!=2:
            print("nincs információ")
        else:
            try:
                felnott=int(ertek[0])
                kolyok=int(ertek[0])
            except:
                print("nincs információ")
            else:
                print("A megfigyelt egyedek száma:{}".format(felnott+kolyok))
        break
    else:
        print("Nincs ilyen feljegyzés")