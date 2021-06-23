# Write a Python program that prints the largest of the values in a dictionary.
# You may assume that all the values in the dictionary are either lists or tuples.
my_dict = {
    "a": [45, 12, 100],
    "b": [4, 0, -4],
    "c": [3, 5, 9],
    "d": [1, 2, 3]
}

max_sum = None

for list_value in my_dict.values():
    list_sum = sum(list_value)

    if max_sum is None:
        max_sum = list_sum
    elif max_sum < list_sum:
        max_sum = list_sum

print(max_sum)
