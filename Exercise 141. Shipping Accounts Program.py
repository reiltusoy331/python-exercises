
print('\t\t\t=== Welcome to the Shipping Accounts Program ===')

customer = input('\nHello, what is your username: ').title()

print(f'\nHello {customer}. Welcome back to your account. ')
print('Current shipping prices are as follows:')

print('\nShipping orders 0 to 100: \t $5.10 each')
print('Shipping orders 101 to 500: \t $5.00 each')
print('Shipping orders 501 to 1000: \t $4.95 each')
print('Shipping orders over 1001: \t $4.80 each')

num_items = int(input('\nHow many items would you like to ship: '))

if num_items == 0 and num_items == 100:
    cost = num_items * 5.10
    print(
        f'To ship {num_items} items it will cost you ${round(cost,2)} at $5.10 per item.')
elif num_items == 101 and num_items == 500:
    cost = num_items * 5.00
    print(
        f'To ship {num_items} items it will cost you ${round(cost,2)} at $5.00 per item.')
elif num_items == 501 and num_items == 1000:
    cost = num_items * 4.95
    print(
        f'To ship {num_items} items it will cost you ${round(cost,2)} at $4.95 per item.')
elif num_items > 1001:
    cost = num_items * 4.80
    print(
        f'To ship {num_items} items it will cost you ${round(cost,2)} at $4.80 per item.')
else:
    print(f'Invalid Input.')

choice = input('\nWould you like to place this order (y/n): ').lower()
if choice == 'y':
    print(f'Okay. Shipping your {num_items} items.')
elif choice == 'n':
    print('Okay, no order is being placed at this time.')
else:
    print(f'Invalid Input.')
