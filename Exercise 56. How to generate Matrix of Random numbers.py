from random import randint

row = 6
column = 12
x = []

for i in range(row):
    y = []
    for j in range(column):
        y.append(randint(1, 100))
    x.append(y)

for i in x:
    for j in i:
        print("%3d" % j, end=' ')
    print()
