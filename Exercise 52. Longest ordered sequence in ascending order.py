from random import random

num = 10

list_item = [0]*num

for i in range(num):
    list_item[i] = int(random()*50)
print(list_item)

maximum = 1
length = 1
mycode = 0

for i in range(1, num):
    if list_item[i] > list_item[i-1]:
        length += 1
    else:
        if length > maximum:
            maximum = length
            mycode = i
        length = 1
print('The maximum length is', maximum)
print('The ordered values are', list_item[mycode-maximum: mycode])
