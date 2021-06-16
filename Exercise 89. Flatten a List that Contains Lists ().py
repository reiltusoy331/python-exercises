# Write a Python program that prints a "flattened" version of a list that contains nested lists.
# "Flattened" means that all the elements in the nested lists should be added to a main list such that it doesn't contain any nested lists, just the individual.
# The list could contain other elements that are not lists or other sequences, so you must check the type of each element and act appropriately.
# If the list is empty, print an empty list.


my_list = [[0, 1, 2], [2, 3, 4], [5, 5, 6]]
flat_list = []

for i in my_list:
    if isinstance(i, list):
        for nested_i in i:
            flat_list.append(nested_i)
    else:
        flat_list.append(i)

print(flat_list)
