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
adatok=[[int[i] for i in sor.split(" ")] for sor in f]
f.close()

print("2. feladat")
print("Az első vendég {}:{}:{}-kor lépett ki az öltözőből.")