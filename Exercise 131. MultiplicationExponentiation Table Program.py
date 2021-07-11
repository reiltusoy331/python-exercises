print('=== Welcome MultiplicationExponentiation Table Program ===')

name = input('Hello, what is your name: ').title().strip()
number = int(input('What number would you like to work with: '))

print(f'\n Multiplication Table For {number}\n')

for i in range(1, 10):
    answer = i*number
    print(f"{i} * {number} = {round(answer,2)}")

print(f'\nExponent Table For {number}\n')
for i in range(1, 10):
    answer = i**number
    print(f"{number} ** {i} = {round(answer,2)}")
