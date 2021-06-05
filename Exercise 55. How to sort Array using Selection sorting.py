from random import randint

x = 5
y = []

for i in range(5):
    y.append(randint(1, 20))
print('the unsorted array:', y)

j = x-1
while j != 0:
    k = 0
    for i in range(1, j+1):
        if y[i] > y[k]:
            k = i
    z = y[k]
    y[k] = y[j]
    y[j] = z
    j -= 1

print('the sorted array:  ', y)
