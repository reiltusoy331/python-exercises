print('\t\t\t=== Welcome to the Voter Registration App ===')

name = input('\nPlease enter your name: ').title()
years_old = int(input('Please enter your age: '))

if years_old <= 17:
    print('\nYou are not old enough to register to vote.')
else:
    print(f'\nCongratulations {name}! You are old enough to register to vote.')
    political_parties = ['Republican', 'Democratic',
                         'Independent', 'Libertatian', 'Green']

    print('\nHere is a list of political parties to join.')
    for party in political_parties:
        print(f'-{party}')

    party = input('\nWhat party would you like to join: ').title()
    if party.startswith('r'):
        print(
            f'\nCongratulations {name}! You have joined the Republican party!')
        print('That is a major party.')
    elif party.startswith('d'):
        print(
            f'\nCongratulations {name}! You have joined the Democratic party!')
        print('That is a major party.')
    elif party.startswith('i'):
        print(
            f'\nCongratulations {name}! You have joined the Independent party!')
        print('That is not major party.')
    elif party.startswith('l'):
        print(
            f'\nCongratulations {name}! You have joined the Libertatian party!')
        print('That is not major party.')
    elif party.startswith('g'):
        print(
            f'\nCongratulations {name}! You have joined the Green party!')
        print('That is not major party.')
    else:
        print('That is not a given party')
