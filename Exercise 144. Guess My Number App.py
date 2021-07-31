import random

print('\t\t\t=== Welcome to the Guess My Number App ===')

player = input('Hello! What is your name: ').title()
print(f'Well {player}, I am thinking of a number between 1 and 20.')

guess_number = random.randint(1, 20)

for num in range(1, 6):
    user_guess = int(input('\nTake a guess: '))

    if user_guess < guess_number:
        print('Your guess is too low.')
    elif user_guess > guess_number:
        print('Your guess is too high.')
    elif user_guess == guess_number:
        break

if user_guess != guess_number:
    print(f'\nGame Over. The number I was thinking of was {guess_number}.')
else:
    print(f'\nGood job, {player}! You guessed my number in {num} guesses.')
