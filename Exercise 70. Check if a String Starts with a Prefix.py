# Write a Python program that checks if the string starts with the sequence of characters denoted by the variable prefix.
# If it does, print True. Else, print False.
# This test should be case sensitive. For example, "A" should not be equivalent to "a".
# If the length of the prefix is greater than the length of the string, print False.


string = "Hello"
prefix = 'He'

# combines string slicing & string comparision
print(string[:len(prefix)] == prefix)


# Option 2 built-in function using "startswith()" method
# string = "Hello"
# prefix = 'He'

# print(string.startswith(prefix))
