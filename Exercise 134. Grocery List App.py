import datetime

time = datetime.datetime.now()
month = str(time.month)
day = str(time.day)
hour = str(time.hour)
minute = str(time.minute)


print('=== Welcome to the Grocery List App ===')

print(f'Current Date and Time: {month}/{day} {hour} {minute}')
print('You currently have Meat and Cheese in your list.\n')

grocery_list = ['Meat', 'Cheese']

item1 = input('Type of food to add to the grocery list: ').title()
grocery_list.append(item1)

item2 = input('Type of food to add to the grocery list: ').title()
grocery_list.append(item2)

item3 = input('Type of food to add to the grocery list: ').title()
grocery_list.append(item3)


print('\nHere is your grocery list:')
print(grocery_list)
print('Here is your grocery list sorted:')
print(sorted(grocery_list))

print('\nSimulating grocery shopping...')

print(f'\nCurrent grocery list: {len(grocery_list)} items')
print(sorted(grocery_list))
remove_item1 = input('\nWhat food did you just buy: ').title()
print(f'Removing {remove_item1} from list..')
grocery_list.remove(remove_item1)


print(f'\nCurrent grocery list: {len(grocery_list)} items')
print(sorted(grocery_list))
remove_item2 = input('\nWhat food did you just buy: ').title()
print(f'Removing {remove_item2} from list..')
grocery_list.remove(remove_item2)


print(f'\nCurrent grocery list: {len(grocery_list)} items')
print(sorted(grocery_list))
remove_item3 = input('\nWhat food did you just buy: ').title()
print(f'Removing {remove_item3} from list..')
grocery_list.remove(remove_item3)


print(f'\nCurrent grocery list: {len(grocery_list)} items')
print(sorted(grocery_list))
no_item = grocery_list.pop()
print(f'\nSorry, the store is out of {no_item}.')
new_item = input('What food would you like instead: ').title()

grocery_list.insert(0, new_item)

print('\nHere is what remains on your grocery list: ')
print(sorted(grocery_list))
