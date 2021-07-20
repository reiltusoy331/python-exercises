
print('\t\t\t=== Welcome Binary\Hexadecimal Conversion App ===')

max_num = int(
    input('\nCompute binary and hexadecimal values up to the ff decimal number: '))

print('Generating lists...complete!')

print('\nUsing slices, we will now show a portion of each list.')
start_num = int(input('What decimal number would you like to start at: '))
stop_num = int(input('What decimal number would you like to stop at: '))

print(f'\nDecimal values from {start_num} to {stop_num}:')
for num in range(start_num, stop_num+1):
    print(num)

print(f'\nBinary values from {start_num} to {stop_num}:')
for num in range(start_num, stop_num+1):
    print(bin(num))

print(f'\nHexadecimaly values from {start_num} to {stop_num}:')
for num in range(start_num, stop_num+1):
    print(hex(num))


input(f'\nPress Enter to see all values from 1 to {max_num}:')
print('Decimal ---- Binary --- Hexadecimal')
for num in range(1, max_num+1):
    print(f"   {num}  ------  {bin(num)}  ------  {hex(num)}")
