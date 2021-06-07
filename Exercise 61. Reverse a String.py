# String Slicing #

# Write a Python Program that prints the reversed version of a string.
# The program must preserve uppercase and lowercase letters.
# If the string is empty, print it intact.


string = 'Hello'


if len(string) == 0:
    print('Empty String.')
else:
    print(string[::-1])
