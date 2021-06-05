from random import random

x = [int(random()*10) for i in range(10)]
print(x)

myset = set(x)  # to make all elements are unique & not repeated


highest = None
frequent = 0

for item in myset:
    frequency = x.count(item)

    if frequency > frequent:
        frequent = frequency
        highest = item

print('The most occurred number is', highest)
