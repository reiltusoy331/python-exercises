# Write a Python program that prints the smallest of three integers a, b, and c.

a = -1
b = -3
c = -4

if (a <= b) and (a <= c):
    print(a, 'is lower than', b, 'and', c)
elif (b <= a) and (b <= c):
    print(b, 'is lower than', a, 'and', c)
else:
    print(c, 'is lower than', a, 'and', b)
