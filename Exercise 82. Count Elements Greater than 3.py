# Write a Python program that counts the number of elements in a list with value greater than 3.
# You may assume that the list only contains numbers.
# Print the final count.


my_list = [1, 2, 3, 5, 6]
counter = 0

for index in my_list:
    if index > 3:
        counter += 1

print(counter)
