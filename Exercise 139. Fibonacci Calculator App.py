print('\t\t\t=== Fibonacci Calculator App ===')

number = int(
    input('\nHow many digits of the Fibonacci sequence would you like to compute: '))

fib = [0, 1]

for i in range(number-2):
    new_fib = fib[i] + fib[i+1]
    fib.append(new_fib)

print(f'\nThe first {number} numbers of the Fibonacci sequence are: ')
for num in fib:
    print(num)
