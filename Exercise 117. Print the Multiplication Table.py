# Write a Python program that prints the multiplication table for a positive integer n.
# The values displayed should go from n x 1 up to n x 10 with a descriptive format (as shown below).
# Use a loop to implement your solution.


print('==== Multiplication Table of 3 ====')

for i in range(1, 11):
    result = i * 3
    print(f"3 x {i} = {result}")
