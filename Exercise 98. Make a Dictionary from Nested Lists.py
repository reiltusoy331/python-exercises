# Write a Python program that creates a dictionary from the values contained in nested lists.
# Each nested list has this format [value1, value2].
# value1 should be the key in the dictionary and value2 should be its corresponding value.
# If there are no nested lists, print an empty dictionary.

my_list = [["a", 1], ["b", 2], ["c", 3], ["d", 4]]

new_dict = {}

for nested_list in my_list:
    key = nested_list[0]
    value = nested_list[1]
    new_dict[key] = value

print(new_dict)
