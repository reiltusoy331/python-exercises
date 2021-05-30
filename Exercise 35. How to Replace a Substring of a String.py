str = "Hello, World, Table, Chair, Cup, Tea"
print(str)

substr1 = input('Choose an old substring to repalce: ')
substr2 = input('Insert new substring: ')
length_substr1 = len(substr1)


while str.find(substr1) > 0:
    i = str.find(substr1)
    str = str[:i] + substr2 + str[i+length_substr1:]

print(str)
