x = abs(int(input('Insert any numbers: ')))

factorial = 1

for i in range(2, x+1):
    factorial *= i

print('The factorial value is ', factorial)
