import random
print('\t\t\t=== Welcome to the Coin Toss App ===')

print('I will flip a coin a set number of times.')
num_flip = int(input('How many times would you like me to flip the coin: '))

show_results = input(
    'Would you like to see the result of each flip(y/n): ').lower()

heads_count = 0
tails_count = 0

for flip in range(num_flip):
    coin = random.randint(0, 1)
    if coin == 1:
        heads_count += 1
        if show_results.startswith('y'):
            print('HEADS')
    else:
        tails_count += 1
        if show_results.startswith('y'):
            print('TAILS')
    if heads_count == tails_count:
        print(
            f'At {flip} flips, the number of heads & tails were equal at {heads_count} each.')


percentage_heads = round(heads_count/num_flip*100, 2)
percentage_tails = round(tails_count/num_flip*100, 2)
print(f'\nResults Of Flipping A Coin {num_flip} Times: \n')

print('Side \t Count \t Percentage')
print(f'Heads \t {heads_count}/{num_flip} \t  {percentage_heads}%')
print(f'Tails \t {tails_count}/{num_flip} \t  {percentage_tails}%')
print()
