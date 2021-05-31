from array import array
from random import randint

x = 20
array = []

for i in range(x):
    array.append(randint(1, 1000))

print('These are the 20 random digits with a highest number of',  max(array))
for i in array:
    print(i, end=' ')

print()
