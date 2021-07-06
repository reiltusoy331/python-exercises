# Write a Python program that prints the digits of a number in reverse order on the same line.
# If the number only has one digit, print this digit.

user_input = int(input(
    "Enter a 3 digit number that will be printed in reverse order: "))

reverse = int(str(user_input)[::-1])


print(reverse)
