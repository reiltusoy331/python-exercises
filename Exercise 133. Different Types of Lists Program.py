print('=== Different Types of Lists Program ===\n')

num_strings = ['15', '100', '55', '42']
num_ints = [15, 100, 55, 42]
num_floats = [2.2, 5.0, 1.245, 0.142857]
num_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(f'The variable num_strings is a {type(num_strings)}.')
print(f'It contains the elements: {num_strings}.')
print(f'The element {num_strings[0]} is a {type(num_strings[0])}.')

print(f'\nThe variable num_ints is a {type(num_ints)}.')
print(f'It contains the elements: {num_ints}.')
print(f'The element {num_ints[0]} is a {type(num_ints[0])}.')

print(f'\nThe variable num_floats is a {type(num_floats)}.')
print(f'It contains the elements: {num_floats}.')
print(f'The element {num_floats[0]} is a {type(num_floats[0])}.')

print(f'\nThe variable num_lists is a {type(num_lists)}.')
print(f'It contains the elements: {num_lists}.')
print(f'The element {num_lists[0]} is a {type(num_lists[0])}.')

print(f'\nNow sorting num_strings and num_ints')
print(f'Sorted num_strings: {sorted(num_strings)}')
print(f'Sorted num_ints: {sorted(num_ints)}')

print(f'\nStrings are sorted alphabetically while integers are sorted numerically!')
