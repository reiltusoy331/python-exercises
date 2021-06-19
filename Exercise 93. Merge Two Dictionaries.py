# Write a Python program that merges two dictionaries and prints the resulting dictionary.
# "Merging" the dictionaries involves making a new dictionary with the key-value pairs in both dictionaries.


dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"c": 4, "d": 6, "e": 8}


merge_dict = {**dict1, **dict2}
# merge_dict = dict1 | dict2  another option using "|" operator in 3.9+ ONLY


print(merge_dict)
