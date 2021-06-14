# Write a Python program that prints the elements of a list followed their corresponding indices.
# Each element and its index must be on the same line separated by a space.
# If the list is empty, print "Empty List".


my_list = [23, 33, 25, 91]

if len(my_list) == 0:
    print("List is Empty")
else:
    print("index  element")
    for index, element in enumerate(my_list):
        print(index, "\t", element)
    # or
    # for i in range(len(my_list)):
    #     print(my_list[i], i)
