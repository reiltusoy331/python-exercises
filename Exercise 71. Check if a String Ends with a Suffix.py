string = "Hello"
suffix = 'llo'

# combines string slicing & string comparision
print(string[-len(suffix):] == suffix)


# Option 2 built-in keyword " in " method

# string = "Hello"
# suffix = 'ello'

# if suffix in string:
#     print(True)
# else:
#     print(False)


# Option 3 built-in function using "endswith()" method
# string = "Hello"
# suffix = 'lo'

# print(string.endswith(suffix))
