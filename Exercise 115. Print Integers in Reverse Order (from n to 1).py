# Write a Python program that prints the integers between a given number n and 1 (in descending order, both inclusive).
# The value of n should be entered by the user and you may assume that it is an integer greater than or equal to 1.
# Use a loop to print each number on a separate line.

user_input = int(input("Enter a value to start the descending order: "))

for i in range(user_input, 0, -1):
    print(i)
