# Write a Python program that reverses the individual words in the string and changes their capitalization.
# Uppercase letters should be printed in lowercase and vice versa.
# Assume that the string only contains letters and spaces are used to separate words.

string = "Hello World"

words_list = string.split()
new_string = ''

for word in words_list:
    reversed_word = word[::-1]
    # built-in keyword " swapcase " method
    swapped_case = reversed_word.swapcase()
    new_string += swapped_case + ' '

new_string.rstrip()
print(new_string)
