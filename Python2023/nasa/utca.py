import random
class telek:
    def __init__(self,sor) -> None:
        vag=sor.split(" ")
        self.oldal=int(vag[0])
        self.szelesseg=int(vag[1])
        self.keritesSzin=vag[2].strip()
        self.hazszam=0

telkek=[]
f=open("kerites.txt")
parosDarab=0
for egySor in f:
    telkek.append(telek(egySor))
    if telkek[-1].oldal==0:
        parosDarab+=1
        telkek[-1].hazszam=parosDarab*2
    else:
        telkek[-1].hazszam=(len(telkek)-parosDarab)*2-1
f.close

print("2. feladat")
print("Az eladott telkek száma: {}".format(len(telkek)))

print("3.feladat")
if telkek[-1].oldal==0:
    print("A páros oldalon adták el az utolsó telket.")
else:
    print("A páratlan oldalon adták el az utolsó telket.")
print("Az urolsó telek házszáma: {}.".format(telkek[-1].hazszam))

print("4. feladat")
elozoSzin="#"
for egyTelek in telkek:
    if egyTelek.oldal==1:
        if egyTelek.keritesSzin!="#" and egyTelek.keritesSzin!=":":
            if egyTelek.keritesSzin==elozoSzin:
                print("A szomszédossal egyezik a kerítés színe: {}".format(egyTelek.hazszam))
                break
            else:
                elozoSzin=egyTelek.keritesSzin

print("5. feladat")
beHazszam=int(input(("Adjon meg egy házszámot")))
hazTalalt=""
for egyTelek in telkek:
    hazTalalt=egyTelek
    if (beHazszam==egyTelek.hazszam):
        if egyTelek.keritesSzin==":":
            print("A kerítés színe / állapota: Nincs kész")
        elif egyTelek.keritesSzin=="#":
            print("A kerítés színe / állapota: Nincs kész")
        else: 
            print("A kerítés színe / állapota: {}".format(egyTelek.keritesSzin))
        break
else:
    print("Nincs ilyen házszám")

if hazTalalt!="":
    hazElotte=""
    hazUtana=""
    for egyTelek in telkek:
        if egyTelek.hazszam==hazTalalt.hazszam-2:
            hazElotte=egyTelek
        if egyTelek.hazszam==hazTalalt.hazszam+2:
            hazUtana=egyTelek

    
    szinek="QWERTZUIOPASDFGHJKLYXCVBNM"
    szinek.replace(hazTalalt.keritesSzin,"")
    if hazElotte!="":
        szinek.replace(hazElotte.keritesSzin,"")
    if hazUtana!="":
        szinek.replace(hazElotte.keritesSzin,"")

    ujSzin=random.choice(szinek)
    print("Egy lehetséges festési szín: {}".format(ujSzin))

f=open("utcakep.txt","w")
for egyTelek in telkek:
    if egyTelek.oldal==1:
        f.write(egyTelek.keritesSzin*egyTelek.szelesseg)
        
f.write("\n")
for egyTelek in telkek:
    if egyTelek.oldal==1:
        f.write(str(egyTelek.hazszam))
        f.write(""*(egyTelek.szelesseg-len(str(egyTelek.hazszam))))
f.close()