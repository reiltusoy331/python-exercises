string = input('Insert some strings: ')

total_strings = string.split()

longest_string = 0

for i in range(1, len(total_strings)):
    if len(total_strings[longest_string]) < len(total_strings[i]):
        longest_string = i

print(total_strings[longest_string])
