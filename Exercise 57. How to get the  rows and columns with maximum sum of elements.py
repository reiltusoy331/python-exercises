from random import random

matrix = []

for i in range(6):
    row = []
    for j in range(6):
        row.append(int(random()*10))
    matrix.append(row)

for row in matrix:
    print(row)

rowmaximum = 0
rowid = 0
i = 0

for row in matrix:
    if sum(row) > rowmaximum:
        rowmaximum = sum(row)
        rowid = i
    i += 1
print(rowid, '=', rowmaximum)

columnmaximum = 0
columnid = 0
for i in range(6):
    sumcolumn = 0
    for j in range(6):
        sumcolumn += matrix[j][i]
    if sumcolumn > columnmaximum:
        columnmaximum = sumcolumn
        columnid = i
print(columnid, '=', columnmaximum)
