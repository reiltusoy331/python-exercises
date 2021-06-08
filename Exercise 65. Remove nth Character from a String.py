# Write a Python program that prints the string without the character at index n.
# If the index num is out of range, print the string intact.
# If the string s is empty, print the string s intact.


string = 'Hello'
num = 1

if (len(string) == 0) or (num >= len(string)):
    print(string)
else:
    new_string = ''
    for i in range(len(string)):
        if i != num:
            new_string += string[i]
    print(new_string)
