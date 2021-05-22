from random import randint

guess_number = randint(1,100)
user_input = -1

trial_period = 1

while guess_number != user_input:
    print('The trial no %d: ' % trial_period, end='')
    user_input = int(input())
    if user_input < guess_number:
        print('The inputted number is less')
    elif user_input > guess_number:
        print('The inputted number is higher')
    else:
        print('Bingo! The inputted number is correct')
    trial_period +=1
