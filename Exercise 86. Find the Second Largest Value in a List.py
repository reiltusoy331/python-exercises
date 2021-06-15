
# Write a Python program that prints the second largest value in a list.
# If the list is empty or only has one element, print None.

my_list = [1, 2, 3, 4, 6]


if not my_list:
    print(None)
else:
    sorted_list = sorted(my_list)
    print('The second largest value in the list is', sorted_list[-2])
