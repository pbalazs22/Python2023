def idoMP(ora,perc,mp):
    return ora*3600+ perc*60 + mp

def idoString(mp):
    ora=mp//3600
    perc=mp%3600//60
    masodperc=mp-ora*3600-perc*60

    return "{:02d}:{:02d}:{:02d}".format(ora,perc,masodperc)

adatok=[]
f=open("furdoadat.txt")
for sor in f:
    darab=sor.split(" ")
    temp=[]
    for egyDarab in darab:
        temp.append(int(egyDarab))
    adatok.append(temp)

f.close()

f=open("furdoadat.txt")
adatok=[[int(i) for i in sor.split(" ")] for sor in f]
f.close()

print("2. feladat")
elsoVendeg=adatok[0]
print("Az első vendég {}:{}:{}-kor lépett ki az öltözőből.".format(elsoVendeg[3],elsoVendeg[4],elsoVendeg[5]))

kilepesek=[]
for egyAdat in adatok:
    if egyAdat[1]==0 and egyAdat[2]==1:
        kilepesek.append(egyAdat)

print("Az utolsó vendég {}:{}:{}-kor lépett ki az öltözőből.".format(kilepesek[-1][3],kilepesek[-1][4],kilepesek[-1][5]))

elozoVendeg=-1
darab=0
negyesek=0
for egyAdat in adatok:
    if egyAdat[0]==elozoVendeg:
        darab+=1
    else:
        if darab==4:
            negyesek+=1
        elozoVendeg=egyAdat[0]
        darab=1

print("3.feladat")
print("A fürdőben {} vendég járt csak egy részlegen.".format(negyesek))
legnagyobbId=0
legnagyobb=0
for egyAdat in adatok:
    if egyAdat[1]==0:
        if egyAdat[2]==1:
            kezdoIdo=idoMP(egyAdat[3],egyAdat[4],egyAdat[5])
        else:  
            vegIdo=idoMP(egyAdat[3],egyAdat[4],egyAdat[5])
            if vegIdo-kezdoIdo>legnagyobb:
                legnagyobb=vegIdo-kezdoIdo
                legnagyobbId=egyAdat[0]
print("4.feladat")
print("A legtöbb időt eltöltő vendég:")
print("{}. vendég {} ".format(legnagyobbId,idoString(legnagyobb)))

stat=[0,0,0]

for egyAdat in adatok:
    if egyAdat[1]==0 and egyAdat[2]==1:
        if egyAdat[3]<9:
            stat[0]+=1
        elif egyAdat[3]<16:
            stat[1]+=1
        else:
            stat[2]+=1


print("5. feladat\n6-9 óra között {} vendég \n 16-20 óra között {}vendég \n9-16 óra között {} vendég".format(*stat))

szaunastat={}
beIdo=0

for egyAdat in adatok:
    if egyAdat[1]==2:
        if egyAdat[2]==0:
            beIdo=idoMP(*egyAdat[3:])
        else:
            if egyAdat[0 not in szaunastat.keys()]:
                szaunastat[egyAdat[0]]=0
            szaunastat[egyAdat[0]]+=idoMP(*egyAdat[3:])-beIdo

f=open("szauna.txt","w")
for egyAdat in szaunastat:
    print(szaunastat[egyAdat])
    f.write("{} {}\n".format(egyAdat,idoString(szaunastat[egyAdat])))

f.close()

reszlegstat=[[],[],[],[],[]]

for egyAdat in adatok:
    if egyAdat[2]==0:
        if egyAdat[0] not in reszlegstat[egyAdat[1]]:
            reszlegstat[egyAdat[1]].append(egyAdat[0])

nevek=["Öltöző","Uszoda","Szaunák","Gyógyvizes medencék","Strand"]
print("7. feladat")
for i in range(len(nevek))[1:]:
    print("{}: {}".format(nevek[i],len(reszlegstat[i])))
