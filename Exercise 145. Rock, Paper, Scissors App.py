import random

print('\t\t\t=== Welcome to the Rock, Paper, Scissors App ===')

rounds = int(input('\nHow many rounds would you like to play: '))

Player = 0
Computer = 0

for round in range(1, rounds+1):
    print(f'\nRound {round}')
    print(f'Player: {Player} \t Computer: {Computer}')

    player_choice = input('Time to pick...rock,paper,scissors: ').lower()
    psr = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(psr)

    print(f'Computer: {computer_choice}')
    print(f'Player: {player_choice}')

    if (player_choice == computer_choice):
        print('It is a tie, how boring! \nThis round was a tie.')

    elif player_choice == 'rock' and computer_choice == 'scissors':

        print('Rock breaks Scissors')
        print(f'You win round {round}')
        Player += 1

    elif player_choice == 'paper' and computer_choice == 'rock':
        print('Paper covers Rock')
        print(f'You win round {round}')
        Player += 1

    elif player_choice == 'scissors' and computer_choice == 'paper':
        print('Scissor cuts Paper')
        print(f'You win round {round}')
        Player += 1

    elif computer_choice == 'rock' and player_choice == 'scissors':
        print('Rock breaks Scissors')
        print(f'You win round {round}')
        Computer += 1

    elif computer_choice == 'paper' and player_choice == 'rock':
        print('Paper covers Rock')
        print(f'You win round {round}')
        Computer += 1

    elif computer_choice == 'scissors' and player_choice == 'paper':
        print('Scissor cuts Paper')
        print(f'You win round {round}')
        Computer += 1
    else:
        print('That is not a valid game option!')
        print('Computer gets the point')
        Computer += 1


print('\nFinal Game Results')
print(f'\tRounds Played: {rounds}')
print(f'\tPlayer Score: {Player}')
print(f'\tComputer Score: {Computer}')
if Player > Computer:
    print('\tWinner: You Win! :-)')
elif Player < Computer:
    print('\tWinner: Computer :-(')
else:
    print('\tWinner: It\'s a Tie :-| ')
