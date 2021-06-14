# Write a Python program that removes all occurrences of the element elem_to_remove from a list.
# The output of the program should be the new list with the element removed.
# If the element is not found in the list, print the message "Not Found".
# If the list is empty, print "Empty List".

my_list = [23, 33, 25, 91]
elem_to_remove = 37


if not my_list:
    print("List is Empty")

elif elem_to_remove not in my_list:
    print("The element to remove not found")

else:
    for element in range(my_list.count(elem_to_remove)):
        my_list.remove(elem_to_remove)

    print(my_list)

# .count() is a list method to  get the number of occurrences of an item.
