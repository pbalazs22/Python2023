print("1. feladat")
hosszabb=[]
szamok=[0,1,2,3,4,5,6,7,8,9]
elso=input("Kérem az első szöveget: ")
masodik=input("Kérem a második szöveget: ")

while True:
    a=input("Kérek egy egész számot: ")
    if a.isnumeric():
        break
a=int(a)

if len(elso) > len(masodik):
    hosszabb.append(elso)
    print("Az első hosszabb")

elif len(elso) < len(masodik):
    hosszabb.append(masodik)
    print("A második hosszabb")

else:
    hosszabb.append(elso)
    print("Az első hosszabb")

for i in range(a):
    print(hosszabb[0])


