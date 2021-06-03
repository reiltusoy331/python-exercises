x = [6, 8, 9, 10, 't', 'tt', 'u', 5]
y = [8, 19, 6, 'tt', 'u', 'z']

# the list function wont function if the list has a sub-list
z = list(set(x) & set(y))

print(z)
