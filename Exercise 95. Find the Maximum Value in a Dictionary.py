# Write a Python program that prints the largest value in a dictionary.
# If the dictionary is empty, print None.
# You may assume that the values are numeric.

my_dict = {"c": 4, "d": 6, "e": 10}

my_dict_sorted = sorted(my_dict.values())

if len(my_dict_sorted) == 0:
    print('None')

else:
    print(my_dict_sorted[-1])


# option 2

# if my_dict_sorted:
#     max_value=max(set(my_dict.valules()))
#     print(max_value)
# else:
#     print(None)
