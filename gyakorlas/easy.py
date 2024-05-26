hosszabb=[]
a=input("Kérem az első szöveget: ")
b=input("Kérem a második szöveget: ")

while True:
    c=input("Kérek egy egész számot: ")
    if c.isnumeric():
        break 
if len(a) > len(b):
    print("Az elso hosszabb")
    hosszabb.append(a)
elif len(a) < len(b):
    print("A masodik hosszabb")
    hosszabb.append(b)
else:
    print("Az elso hosszabb")
    hosszabb.append(a)

for i in range(int(c)):
    print(*hosszabb)



  
    




