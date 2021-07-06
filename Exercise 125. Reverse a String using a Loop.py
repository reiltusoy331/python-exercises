# Write a Python program that prints a string reversed using a loop.
# All the characters must be on the same line in reverse order.

user_input = input("Enter a word that will be printed in reverse order: ")

for char in reversed(user_input):
    print(char, end='')
