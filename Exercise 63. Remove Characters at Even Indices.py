# Write a Python program that prints the string without the characters located at even indices.
# If the string is empty or only has one character, print it intact.

string = 'Programming'

new_string = ''

for i in range(len(string)):
    if i % 2 != 0:
        new_string += string[i]

print(new_string)

# option 2
# for i in range(1,len(string),2):
