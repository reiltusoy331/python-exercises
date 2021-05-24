print('Zero Terminates Program')

while True:
    operator = input('Choose Operator(+, -, *, /): ')
    if operator == 'o' or operator=='O':
        break
    if operator in ('+', '-', '*', '/'):
       num1 = float(input('Enter the value of first number: ')) 
       num2 = float(input('Enter the value of second number: ')) 
       if operator == '+':
           print("%.2f" % (num1+num2))
       elif operator == '-':
           print("%.2f" % (num1-num2))
       elif operator == '*':
           print("%.2f" % (num1*num2))
       elif operator == '/':
           if num2 != 0:
              print("%.2f" % (num1/num2)) 
           else:
               print("Error! Division by Zero")
       else:
            print("Invalid Operator")



        