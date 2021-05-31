string = input('Insert a word: ')

length_string = len(string)

for i in range(length_string//2):
    if string[i] != string[-1-i]:
        print('This is NOT a palindrome')
        quit()

print('This is a palindrome')

# s = "Hello World"
# s = s[-1-1]
# print(s)
