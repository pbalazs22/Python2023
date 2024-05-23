dobasok=[3, 1, 1, 2, 1, 5, 5, 4, 4, 4, 1, 2, 3, 6, 4, 6, 1, 4]
pozicio=[]
kezdo=0
for lepes in dobasok:
    kezdo+=lepes
    if str(kezdo)[-1] == "0":
        kezdo-=3
    pozicio.append(kezdo)

print(pozicio)



    
