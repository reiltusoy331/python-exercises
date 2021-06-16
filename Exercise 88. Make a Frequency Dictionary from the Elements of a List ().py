# Write a Python program that creates and print a dictionary that maps each element in a list to its
# corresponding frequency (how many times it occurs in the list).
# The test should be case-sensitive. Therefore, "A" should not be considered the same element as "a".


my_list = [0, 1, 2, 2, 3, 4, 5, 5, 6]

counter_dict = {}

for i in my_list:
    if i not in counter_dict:
        counter_dict[i] = 1
    else:
        counter_dict[i] += 1

print(counter_dict)
