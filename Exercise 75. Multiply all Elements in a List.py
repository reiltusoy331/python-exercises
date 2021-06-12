# Write a Python program that multiplies all the items in a list by the value of the variable factor.
# The program must print the list as the output.
# The program should also allow multiplying the variable factor by a string in case the list contains strings.
# You may assume that the value of factor will be a positive integer.

my_list = [3, 4, 5, 6]
factor = 2

for i in range(len(my_list)):
    my_list[i] *= factor

print(my_list)

# Option 2
# built-in function using "enumerate(list)" method
# enumerate method will  return a sequence of index with its corresponding value of that index
# my_list = [3, 4, 5, 6]
# factor = 2

# for i, element in enumerate(my_list):
#     my_list[i] = element * factor

# print(my_list)
