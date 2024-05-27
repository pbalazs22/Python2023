lista=[]

szokoz=" "
while True:
    a=input("Adj egy szót: ")

    if len(a) >= 10 and szokoz not in a:
        lista.append(a)
    elif a == "":
        break

tobbi="-".join(lista[:-1])

print(lista[-1])
print("-".join(lista[:-1]))

