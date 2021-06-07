
# Write a Python program that prints the character at index i in the string s.
# If the index is out of range, the program should print "i is out of range"
# If the string is empty, the program should print "Empty String"


string = "hello"
i = 2

if len(string) == 0:
    print(string[i], 'Empty String.')
elif i < len(string):
    print(string[i])
else:
    print('is out of range.')
