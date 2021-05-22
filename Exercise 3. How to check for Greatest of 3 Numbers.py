x = int(input('Enter the first number: '))
y = int(input('Enter the second number: '))
z = int(input('Enter the three number: '))

if x > y and x > z:
    print('the maximum number is: ',x)
elif y > x and y > z:
    print('the maximum number is: ',y)
elif z > x and z > y:
    print('the maximum number is: ',z)
else:
    print('Enter a valid number or input')




 