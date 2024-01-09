adat=[]
f=open("fob2016.txt", "r")
for sorr in f:
    adat.append(sorr.strip())

f.close()


f=open("fob2016.txt")
for sorr in f:
     adat.append(sorr.split())

f.close()
print(adat)






