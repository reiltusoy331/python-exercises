x = 1

while x < 11:
    y = 1
    while y < 11:
        print('%4d' % (x*y), end='')
        y+=1
    print()
    x += 1