adatok=[]

f=open("tancrend.txt")
for sor in f:
    adatok.append(sor.strip())

f.close()
print(adatok)

tancok=adatok[::3]
lanyok=adatok[1::3]
fiuk=adatok[2::3]
#print (tancok)