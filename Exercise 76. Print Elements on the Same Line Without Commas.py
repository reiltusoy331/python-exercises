# Write a Python program that prints the elements of a list on the same line.
# The elements should be separated only by a space (not by a comma).
# The output should not include the opening and closing square brackets [ ].


my_list = ["3", "4", "5", "6", "7"]
for i in my_list:
    print(i, end=' ')


# Option 2
# unpacking the my_list by *my_list
#
# my_list = ["3", "4", "5", "6", "7"]
# print(*my_list, sep=' )
