lista=["csoki","habcsók","négercsók","csokisbanán","gumicukor"]

#print(lista)

for elem in lista:
    print(elem)
    
print("-"*30)

for elem in lista[:2]:
      print(elem)

print("-"*30)

for elem in lista[-2:]:
      print(elem)

print("-"*30)

for elem in lista[1::2]:
      print(elem)

print("-"*30)

for elem in lista[::-1]:
      print(elem)

print("-"*30)

for elem in lista[1::2]:
      print(elem)

lista2=lista[:3]
print(lista2)


