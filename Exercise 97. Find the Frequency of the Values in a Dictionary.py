# Write a Python program that counts the frequency of each value in a dictionary.
# The program should create a new dictionary to map each value in the original
# dictionary to its frequency (how many times it occurs).
# If the dictionary is empty, print an empty dictionary.

my_dict = {
    "a": 4,
    "b": 4,
    "c": 2,
    "d": 7,
    "e": 4,
    "f": 2,
    "g": 7,
    "h": 7
}

freq_dict = {}

for value in my_dict.values():
    if value in freq_dict:
        freq_dict[value] += 1
    else:
        freq_dict[value] = 1

print(freq_dict)
