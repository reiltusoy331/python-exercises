# Write a Python program that calculates the factorial of a given number n.
# The value of n should be entered by the user.
# The program must print the result and use a loop to calculate it.

number = int(input("Enter a number to calculate the factorial: "))

factorial = 1

for i in range(2, number+1):
    factorial *= i

print(f"The factorial value of !{number} is", factorial)
