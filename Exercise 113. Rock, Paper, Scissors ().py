# Write a Python program that simulates the "Rock, Paper, Scissors" game.
# The game should ask the user to enter an option (either "Rock", "Paper", or "Scissors").
# The player should play against the computer, which will select a random option.
# The computer's selection will be compared against the player's selection to determine who wins.
# A descriptive message should be displayed indicating if the player won, lost, or if the game
# ended in a tie.
# Basic Game Rules:
# Paper beats Rock
# Rock beats Scissors
# Scissors beat Paper.
from random import randint

Rock = 1
Paper = 2
Scissors = 3

print("====== Welcome to the game ======")
player_choice = input(
    "Please enter Rock, Paper, or Scissors below: \n").capitalize()

computer_choice = randint(1, 3)

if player_choice == "Rock":
    if computer_choice == 1:
        print(computer_choice)
        print("It's a tie! Try again.")
    elif computer_choice == 2:
        print(computer_choice)
        print("You lose! Your opponent chose 'Paper'")
    elif computer_choice == 3:
        print(computer_choice)
        print("You Win! Your opponent chose 'Scissors'")

elif player_choice == "Paper":
    if computer_choice == 1:
        print(computer_choice)
        print("You Win! Your opponent chose 'Rock'")
    elif computer_choice == 2:
        print(computer_choice)
        print("It's a tie! Try again.")
    elif computer_choice == 3:
        print(computer_choice)
        print("You lose! Your opponent chose 'Scissors'")

elif player_choice == "Scissors":
    if computer_choice == 1:
        print(computer_choice)
        print("You lose! Your opponent chose 'Rock'")
    elif computer_choice == 2:
        print(computer_choice)
        print("You Win! Your opponent chose 'Paper'")
    elif computer_choice == 3:
        print(computer_choice)
        print("It's a tie! Try again.")
else:
    print("Invalid Input")
