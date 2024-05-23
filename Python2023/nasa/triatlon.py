adatok=[]
f=open("triatlon.txt")
for egysor in f:
    darab=egysor.strip().split(";")
    adatok.append(darab)
f.close


print("1.feladat")
print(adatok)
print("2. feladat")
print("A versenyen {}-en vettek részt".format(len(adatok)-1))



class triatlon:
    def __init__(self,nev,nem,szuletesnap,uszas,kerekpar,futas,rajtszam) -> None:
        self.nev=nev
        self.nem=nem
        self.szuletesnap=szuletesnap
        self.uszas=uszas
        self.kerekpar=kerekpar
        self.futas=futas
        self.rajtszam=rajtszam

f=open("osszidok.txt","x")





        
    


    