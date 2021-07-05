# Write a Python program that prints a triangular pattern like the ones shown below in the examples.
# Each row must have its corresponding number of asterisks. The first row contains one asterisk.
# The second row contains two asterisks. The third row contains three asterisks and so on.
# The number of rows should be determined by the value of n, a value entered by the user.

number = int(input("Enter a number to print a triangular pattern: "))

for i in range(1, number+1):
    print('* '*i)


# pattern = 0
# for i in range(1, number+1):
#     pattern = + i
#     print('* '*pattern, end='\n')
