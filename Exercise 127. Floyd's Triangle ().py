# Write a Python program that prints Floyd's Triangle with n number of rows.
# The value of n should be entered by the user. You may assume that it is a positive integer.
# Floyd's Triangle is made with consecutive numbers that fill the rows of the triangle (as shown below).

number = int(input("Enter a number of row for Floyd's triangle: "))

counter = 1

for i in range(1, number+1):  # number of rows
    for j in range(0, i):  # number of iteration to be printed per row
        print(counter, end=" ")
        counter += 1
    print()
