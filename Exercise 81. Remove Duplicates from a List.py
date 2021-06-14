# Write a Python program that removes duplicate elements from a list, only keeping one occurrence of each element in the list.
# The original list should be mutated(modified).
# The program must print the final version of the list.

my_list = [23, 23, 33, 25, 91]

remove_dups = list(set(my_list))
print(remove_dups)


# Sets is a data structure commonly used to remove duplicates from lists and tuples in Python.
# Another user method is using "dict.fromkeys(my_list)"
