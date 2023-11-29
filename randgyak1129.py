import random

tamas=[]

for i in range(random.randrange(15,21)):
    tamas.append(random.randrange(1,6))


print(tamas)
print(sum(tamas)/len(tamas))