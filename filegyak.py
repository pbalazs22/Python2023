f=open("sanyi.txt","w")
for i in range(100):
    f.write(str(i)+"\n")
f.close()


f=open("sanyi.txt","r")
lista=[]
for egySor in f:
    lista.append(egySor.strip())
f.close()
print(lista)

f=open("sanyi.txt","r")
szoveg=f.read()
#szoveg=szoveg.strip()
#lista=szoveg.strip().split("\n")  
lista=szoveg.split("\n")[:-1]
f.close()
print(lista)

osszeg=0
for egySzam in lista:
    osszeg+=int(egySzam)

print(osszeg)

lista2=[]
f=open("sanyi.txt")
for egySzam in f:
    lista2.append(int(egySzam))
f.close()
print(lista2)