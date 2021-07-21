import math

print('\t\t\t=== Factorial Calculator App ===')

number = int(
    input('\nWhat number would you like to compute the factorial of? '))

factorials = 1
fact_list = []
separator = '*'

for num in range(1, number+1):
    factorials *= num
    fact_list.append(str(num))

print(f'{number}! = {separator.join(fact_list)}')

print('\nHere is the result from the math library.')
print(f'The factorial of {number} is {math.factorial(number)}.')

print('\nHere is the result from my own algorithm.')
print(f'The factorial of {number} is {factorials}.')
