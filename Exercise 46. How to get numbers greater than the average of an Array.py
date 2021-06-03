import random


x = 5
y = []
avg = 0

for i in range(x):
    y.append(random.random())
    print('%5.2f' % y[i], end=' ')
    avg += y[i]
print()

average = avg/x
print('The average of the array is %.2f' % average)
for i in y:
    if i > average:
        print('%4.2f' % i)
