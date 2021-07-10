# Write a Python program that prints a triangular pattern made with letters.
# The first row should have one letter A (in uppercase). The second row should have two letters B.
# The third row should have three letters C and so on.
# The number of rows is determined by the value of n, which is entered by the user.
# The letters must be separated by a space.

number = int(input("Enter a number of row for triangular letters: "))

counter = 65

for i in range(1, number + 1):
    for j in range(i):
        print(chr(counter), end=' ')
    counter += 1
    print()


# option 2

# for i in range(number):
#     print(chr(65+i)*(i+1))
