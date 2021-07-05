# Write a Python program that checks if a number is prime or not.
# If the number is prime, it should print "Prime".
# If the number is not prime, it should print "Not prime".

number = int(input("Enter a number to check if it's prime number: "))

if number == 0 or number == 1:
    print('Not Prime')

else:
    for i in range(2, number):
        if number % i == 0:
            print('Nor Prime')
            break
        else:
            print('Prime')
