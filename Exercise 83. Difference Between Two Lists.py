# Write a Python program that prints (as a list) the elements of listA that are not in listB as a list.
# If the lists have the same elements, print an empty list.
# If listA is an empty list, print an empty list.

listA = [1, 2, 3, 4]
listB = [1, 2]
new_list = []


for i in listA:
    if i not in listB:
        new_list.append(i)

print(new_list)
