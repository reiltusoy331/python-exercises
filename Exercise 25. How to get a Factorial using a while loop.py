x = abs(int(input('Insert any numbers: ')))

factorial = 1
counter = x

while counter > 1:
    factorial *= counter
    counter-= 1

print(x, 'has a factorial value of', factorial)
