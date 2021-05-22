x = float(input('Enter a coordinate of point x: '))
y = float(input('Enter a coordinate of point y: '))


if x > 0 and y > 0:
    print('The first quadrant')
elif x < 0 and y > 0:
    print('The second quadrant')
elif x < 0 and y < 0:
    print('The third quadrant')
elif x < 0 and y < 0:
    print('The fourth quadrant')
elif x == 0 and y == 0:
    print('The point of origin')
elif x == 0:
    print('x point')
elif y == 0:
    print('y point')
