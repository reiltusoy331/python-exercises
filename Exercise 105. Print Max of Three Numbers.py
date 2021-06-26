# Write a Python program that prints the maximum of three integers (a, b, c).

a = 3
b = 5
c = 8

if (a >= b) and (a >= c):
    print(a, 'is greater than', b, 'and', c)
elif (b >= a) and (b >= c):
    print(b, 'is greater than', a, 'and', c)
else:
    print(c, 'is greater than', a, 'and', b)
