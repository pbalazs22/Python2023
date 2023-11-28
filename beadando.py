import random
#1. feladat
szamok = [random.randint(10000, 99999) for l in range(500)]
print(szamok)

print("-"*80)
#2. feladat
parosszamok= len([szam for szam in szamok if szam % 2 == 0])
print(parosszamok)

print("-"*80)
#3. feladat
paratlanszamok= 0
for szam in szamok:
    if szam % 2 != 0:
        paratlanszamok+= szam
print("A generált számok páratlan számainak összege:", paratlanszamok)

print("-"*80)
#5. feladat
harmaskezd= len([szam for szam in szamok if 30000< szam <39999])
print(harmaskezd)

print("-"*80)
#6. feladat
egyszamjegy=len([szam for szam in szamok if 10000< szam <19999])
print("1-es számjegy kezdetű számból van:",egyszamjegy)

kettoszamjegy=len([szam for szam in szamok if 20000< szam <29999])
print("2-es számjegy kezdetű számból van:",kettoszamjegy)

haromszamjegy=len([szam for szam in szamok if 30000< szam <39999])
print("3-as számjegy kezdetű számból van:",haromszamjegy)

negyszamjegy=len([szam for szam in szamok if 40000< szam <49999])
print("4-es számjegy kezdetű számból van:",negyszamjegy)

otszamjegy=len([szam for szam in szamok if 50000< szam <59999])
print("5-ös számjegy kezdetű számból van:",otszamjegy)

hatszamjegy=len([szam for szam in szamok if 60000< szam <69999])
print("6-os számjegy kezdetű számból van:",hatszamjegy)

hetszamjegy=len([szam for szam in szamok if 70000< szam <79999])
print("7-es számjegy kezdetű számból van:",hetszamjegy)

nyolcszamjegy=len([szam for szam in szamok if 80000< szam <89999])
print("8-as számjegy kezdetű számból van:",nyolcszamjegy)

kilencszamjegy=len([szam for szam in szamok if 90000< szam <99999])
print("9-es számjegy kezdetű számból van:",kilencszamjegy)


