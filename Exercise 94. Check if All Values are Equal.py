# Write a Python program that checks if all values in a dictionary are equal.
# If they are, print True. Else, print False.
# If the dictionary is empty, print "Empty".

my_dict = {"a": 2, "b": 2, "c": 2}

# values() is a dictionary method the gets the value only not the key pair value
num_uniq_values = len(set(my_dict.values()))

if num_uniq_values == 0:
    print('Empty')

elif num_uniq_values == 1:
    print('True')

else:
    print('False')
