mdv = input('Enter a value to calculate(m,d,v): ')

if mdv =='m':
    d = float(input('Density: '))
    v = float(input('Volume: '))
    result = d*v #This is for mass only

elif mdv =='d':
    m = float(input('Mass: '))
    v = float(input('Volume: '))
    result = m/v #This is for density only
elif mdv =='v':
    m = float(input('Mass: '))
    d = float(input('Density: '))
    result = m/d #This is for mass only
else:
    print("Invalid input")

print("%.2f" % result)