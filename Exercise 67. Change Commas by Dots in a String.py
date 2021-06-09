# Write a Python program that prints a version of the string with all commas replaced by dots.

string = "3,456,123"
new_string = ''

comma = ','
dot = '.'


for char in string:
    if char == comma:
        new_string += dot
    else:
        new_string += char


print(new_string)


# Option 2 built-in function using "replace()" method

# string = "Hello, World!"

# comma = ','
# dot = '.'

# print(string.replace(comma, dot))
