lista=[]
be=1

while be!=0:
    try:
        be=int(input ("kerek egy számot:"))
        if be!=0:
            lista.append(be)
    except:
        pass

print(lista)
lista2=lista[2:-2]
print(lista2)
