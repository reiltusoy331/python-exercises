# Write a Python program that checks if a key exists in a dictionary or not.
# If the key exists in the dictionary, print True. Else, print False.
# The key should be stored in the variable key.

my_dict = {"a": 1, "b": 2, "c": 3}
key = "c"

if key in my_dict:
    print(True)
else:
    print(False)


# other option
# my_dict = {"a": 1, "b": 2, "c": 3}
# key = "c"
# print(key in my_dict)
