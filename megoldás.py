adatok=[]
f=open("fob2016.txt")
for sor in f:
    adatok.append(sor.strip().split(" "))

f.close()

for i in range(len(adatok)):
    adatok[i][0]=int(adatok(i)[0])