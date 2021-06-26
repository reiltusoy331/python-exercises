# Write a Python program that prints the corresponding season based on the value of the variable season_num.
# The possible values of season_num are: 1 for Spring, 2 for Summer, 3 for Fall, 4 for Winter.
# If the value of season_num is neither one of these values, print "Please enter a valid number".

seasons = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}

season_num = 4

if season_num in seasons:
    print(seasons[season_num])
else:
    print("Please enter a valid number")
