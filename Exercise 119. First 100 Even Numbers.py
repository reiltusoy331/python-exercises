# Write a Python program that prints the first 100 even numbers (from 2 to 200 inclusive).

for n in range(1, 201):
    if n % 2 == 0:
        print(f"{n}")

# OPTION 2

# for n in range(2, 202, 2):
#     print(f"{n}")
