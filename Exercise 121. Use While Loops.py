# Try to implement the previous exercises using While loops.

number = int(input("Enter a number to calculate the factorial: "))

factorial = 1
i = 1

while i < number+1:
    factorial *= i
    i += 1

print(f"The factorial value of !{number} is", factorial)
