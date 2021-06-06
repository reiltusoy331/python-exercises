from random import randint

column = 5
row = 5
matrix = []
sum_column = [0]*column
sum_row = [0]*row


for i in range(row):
    myrow = []
    for j in range(column):
        myrow.append(randint(0, 3))
    matrix.append(myrow)

for i in range(row):
    for j in range(column):
        sum_row[i] += matrix[i][j]
        sum_column[j] += matrix[i][j]

for i in range(row):
    print(matrix[i], "|", sum_row[i])

print("-" * column*4)
print(sum_column)
