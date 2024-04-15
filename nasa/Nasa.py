class keres:
    def __init__(self,cim,ido,kep,status,meret):
        self.cim=cim
        self.ido=ido
        self.kep=kep
        self.status=status
        self.meret=meret

        self.kepNEV=self.kep.split("/")[-1]
    def ByteMeret(self):
        szam=0

        
        if self.meret!="-":
            szam=int(self.meret)

        return szam
    
    def Domain(self):
        try:
            int(self.cim[-1])
            return False
        except:
            return True
        


#másképpen 
        return not self.cim[-1] in "0123456789"
    
class adatok(keres):
    def __init__(self,sor):
        vag=sor.split("*")
        vag2=vag[-1].split(" ")
        super().__init__(vag[0],vag[1],vag[2],vag2[0],vag2[1])

f=open("NASAlog.txt")
log=[]
for egySor in f:
    print(egySor)
    log.append(adatok(egySor.strip()))
f.close()

print(log[0].cim)

print("5. feladat: Kérések száma: {}".format(len(log)))
osszeg=0
for elem in log:
    osszeg+=elem.ByteMeret()


print("6. feladat: Válaszok mérete összesen: {} byte".format(osszeg))

darab=0
for elem in log:
    if elem.Domain():
        darab+=1


print("8. feladat: Domain-es kérések: {:.2%}".format(darab/len(log)))

stat={}
for elem in log:
    if elem.status not in stat.keys():
        stat[elem.status]=0

    stat[elem.status]+=1

print("9. feladat: Statisztika")
for kulcs in stat.keys():
    print("\t{}:{}db".format(kulcs,stat[kulcs])) 

stat={}
for elem in log:
    if elem.ora not in stat.key():
        stat[elem.ora]=0
    stat[elem.ora]+=1


print("10.feladat")
for kulcs in stat.keys():
    print("\t{}:{}db".format(kulcs,stat[kulcs]))


