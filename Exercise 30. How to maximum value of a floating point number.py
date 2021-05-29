# from random import random

# x = round(random()*1000,3)
# print(x)

x = float(input('Insert floating point number only: '))

y = str(x)
maximum = -1


for i in range(len(y)):
    if y[i]  == '.':
        continue
    elif maximum < int(y[i]):
        maximum = int(y[i])

print('The maximum element is = ',maximum)
