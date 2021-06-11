# Write a Python program to convert a string s to lowercase, sort the characters of each
# word in alphabetical order, and print the resulting string.
# You may assume that the string only contains letters and spaces to separate the words.
# Spaces should be preserved in the final string.

string = "Hello World"
new_string = ''

words_list = string.split()

for word in words_list:
    lowercase_word = word.lower()
    sorted_word = ''.join(sorted(lowercase_word))
    new_string += sorted_word+" "

new_string.rstrip()
print(new_string)
