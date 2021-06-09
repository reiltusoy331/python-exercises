# Write a Python program that prints a copy of the string without any spaces.
# Words should be connected in the final string.
# If the string doesn't contain spaces, print it intact.


string = "Python Prog rammin g"
new_string = ''

space = ' '

for char in string:
    if char != space:
        new_string += char
    # else:
    #     pass

print(new_string)
