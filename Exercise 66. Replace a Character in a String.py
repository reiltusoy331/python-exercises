# Write a Python program that prints the string with the character curr_char replaced by the character new_char.
# curr_char and new_char are variables that contain strings with a single character.
# You may assume that new_char will not be an empty string.
# The match must be case-sensitive (do not replace lowercase letters if curr_char is uppercase).
# If no match is found, print the initial string.


string = 'Hello'
new_string = ''

curr_char = 'l'
new_char = 's'


for char in string:
    if char == curr_char:
        new_string += new_char
    else:
        new_string += char

print(new_string)


# option 2 built-in function

# string = 'Hello'
# curr_char = 'l'
# new_char = 's'

# print(string.replace(curr_char, new_char))
