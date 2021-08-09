import random
print('\t\t\t=== Welcome to the Thesaurus App ===')

print('Choose a word from the thesaurus and I will give you a synonym.')

thesaurus = {
    'hot': ['balmy', 'summery', 'tropical', 'boiling', 'scorching'],
    'cold': ['chilly', 'cool', 'freezing', 'frigid', 'polar'],
    'happy': ['content', 'cheery', 'merry', 'jovial', 'jocular'],
    'sad': ['unhappy', 'downcast', 'miserable', 'glum', 'melancholy']
}


print('Here are the words in the thesaurus: ')
for word in thesaurus.keys():
    print(f'\t-{word}')

user_input = input('What word would you like a synonym for: ').lower().strip()

if user_input in thesaurus:
    index = random.randint(0, 4)
    print(f'A synonym for {user_input} is {thesaurus[user_input][index]}')
else:
    print('The selected word is not in the choices.')

print_thesaurus = input(
    'Would you like to see the whole thesaurus(\'yes/no\'): ').lower().strip()

if print_thesaurus == 'yes':
    for key, values in thesaurus.items():
        print(f'\n {key.title()} synonyms are: ')
        for value in values:
            print(f'\t- {value}')
else:
    print('I hope you enjoyed this app.')
