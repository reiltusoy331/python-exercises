x = input('Enter a temperature in \'C\' or \'F\' : ')

unit = x[-1]
x = int(x[0:-1])

if unit == 'C' or unit == 'c':
    x = round(x*(9/5)+32) 
    print(str(x)+'C')

elif unit == 'F' or unit == 'f':
    x = round((x-32)*(5/9)) 
    print(str(x)+'F')
else:
    print('Invalid Input')

