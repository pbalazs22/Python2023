import random

def vel(mettol,meddig,lepes=1):
    darab=((meddig-mettol)/lepes)//1+1
    if((meddig-mettol)/lepes)%1!=0:
        darab+=1

    eltolas=mettol

    szam=lepes*((random.random()*darab)//1)+eltolas    
    
    return szam

print(vel(0,10))    



magas=[]
for i in range(int(vel(15,38))):
    magas.append(vel(150,200))

print(magas)