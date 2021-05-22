import math

x = float(input('Insert point x: '))
y = float(input('Insert point y: '))
rad = float(input('Insert the radius: '))

hypothenus = math.sqrt(pow(x,2) + pow(y,2))

if hypothenus <= rad:
    print('The point belongs to circle.')
else:
    print('The point does not belongs to circle.')