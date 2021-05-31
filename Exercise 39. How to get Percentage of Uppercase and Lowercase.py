string = input('Insert some words of Uppercase and Lowercase: ')

length_strings = len(string)

uppercase = lowercase = 0


for i in string:
    if 'a' <= i <= 'z':
        lowercase += 1
    elif 'A' <= i <= 'Z':
        uppercase += 1

print('Percentage of Uppercase: %.2f %%' % (uppercase/length_strings*100))
print('Percentage of Lowercase: %.2f %%' % (lowercase/length_strings*100))
