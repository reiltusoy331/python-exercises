# Write a Python program that prints a pyramid pattern made with asterisks.
# The number of rows should be determined by the value of the variable n.
# This value will be entered by the user.
# You may assume that the value of n is a positive integer.

number = int(input("Enter a number to print a triangular pattern: "))

for i in range(1, number+1):
    spaces = number - i
    print(' '*spaces, '*'*i)
