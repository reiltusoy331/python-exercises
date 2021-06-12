# Write a Python program that prints the largest and smallest values in a list
# Print the two values on the same line, separated by a space.
# The largest value should appear first and the smallest value should appear second.
# You may assume that the list only contains numeric values.
# If the list is empty, print None.

my_list = ["3", "4", "5", "6", "7"]
largest = ''
smallest = ''

if my_list != None:
    largest = max(my_list)
    smallest = min(my_list)
    print(largest, smallest)
    # or
    #print(max(my_list), min(my_list))
else:
    print(None)
