import random
szo=""
maganhangzo=("öüóeuioőúaéáűí")
massalhangzo=("qwrtzpsdfghjklyxcvbnm")
x=("öüóqwertzuiopőúasdfghjkléáűíyxcvbnm")
print(''.join(random.choices(x,k=5)))
szo+=random.choice(list(x))
print(szo)
