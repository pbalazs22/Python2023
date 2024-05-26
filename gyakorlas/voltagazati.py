print("1.feladat")
sor=input("Sorok száma: ")
oszlop=input("Oszlopok száma: ")

while True:
    karakter=input("Kérek pontosan 1 karaktert: ")
    if len(karakter) == 1:
        break
    else:
        print("Nem megfelelő méret!")

kiiras=int(oszlop)

a=(karakter * int(sor))
for i in range(kiiras):
    print(a) 


