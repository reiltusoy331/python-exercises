# Write a Python program that creates and displays a dictionary that maps each letter
# in a string to how many times the character occurs in the string (its frequency).
# The dictionary should only include the characters in the string.
# The test should be case-insensitive ("A" should be counted as "a").
# The keys in the dictionary should be lowercase letters.
# Only include letters in the dictionary.

string = "Hello, World"

freq_dict = {}

for char in string.lower():
    if char.isalpha():
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1

print(freq_dict)
