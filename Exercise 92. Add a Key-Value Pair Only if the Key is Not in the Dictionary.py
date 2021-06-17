# Write a Python program that adds a new key-value pair to a dictionary only if the key doesn't exist already.
# If the key-value pair exists in the dictionary, do not update the existing value. The dictionary should not be modified in this case.
# Store the new key in the new_key variable and the new value in the new_value variable.
# Print the final value of the dictionary.

my_dict = {"January": 45, "February": 56, "March": 67}

new_key = "April"
new_value = 27

if new_key not in my_dict:
    my_dict[new_key] = new_value
    print(my_dict)
else:
    print('The key already exists in the dictionary')


# option 2
# if new_key not in my_dict:
#     my_dict.update({new_key: new_value})
#     print(my_dict)
# else:
#     print('The key already exists in the dictionary')
