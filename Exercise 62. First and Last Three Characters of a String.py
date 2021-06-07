# Write a Python program that prints the first and last three characters of the string s as a single string.
# If the string has less than six characters, print an empty string (blank output).


string = 'Programming'


if len(string) < 6:
    print(" "" ")
else:
    first_character = string[:3]
    last_three_characters = string[-3:]
    print(first_character + last_three_characters)


# other option
# new_string = s[:3] + s[len(s)-3:]
# print(new_string)
