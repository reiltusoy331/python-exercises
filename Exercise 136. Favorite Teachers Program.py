print('\t\t\t=== Favorite Teachers Program ===')

teachers = []

teacher = input('\nWho is your first favorite teacher: ').title()
teachers.append(teacher)
teacher = input('Who is your second favorite teacher: ').title()
teachers.append(teacher)
teacher = input('Who is your third favorite teacher: ').title()
teachers.append(teacher)
teacher = input('Who is your fourth favorite teacher: ').title()
teachers.append(teacher)

print(f'\nYour favorite teachers ranked are: {teachers}')
sort_teachers = sorted(teachers)
print(f'Your favorite teachers alphabetically are: {sort_teachers}')
sort_teachers = sorted(teachers, reverse=True)
print(
    f'Your favorite teachers in reverse alphabetically order are: {sort_teachers}')

print(f'\nYour top two teachers are: {teachers[0]} and {teachers[1]}')
print(f'Your next two teachers are: {teachers[2]} and {teachers[3]}')
print(f'Your last favorite teacher is: {teachers[3]}')
print(f'You have a total of {len(teachers)} favorite teachers.')


teacher = input(
    f'\nOops, {teachers[0]} is no longer your first favorite teacher. Who is your new FAVORITE teacher: ').title()
teachers.insert(0, teacher)


print(f'\nYour favorite teachers ranked are: {teachers}')
sort_teachers = sorted(teachers)
print(f'Your favorite teachers alphabetically are: {sort_teachers}')
sort_teachers = sorted(teachers, reverse=True)
print(
    f'Your favorite teachers in reverse alphabetically order are: {sort_teachers}')

print(f'\nYour top two teachers are: {teachers[0]} and {teachers[1]}')
print(f'Your next two teachers are: {teachers[2]} and {teachers[3]}')
print(f'Your last favorite teacher is: {teachers[3]}')
print(f'You have a total of {len(teachers)} favorite teachers.')


teacher = input(
    '\nYou\'ve decided you no longer like a teacher. Which teacher would you like to remove from your list: ').title()

teachers.remove(teacher)

print(f'\nYour favorite teachers ranked are: {teachers}')
sort_teachers = sorted(teachers)
print(f'Your favorite teachers alphabetically are: {sort_teachers}')
sort_teachers = sorted(teachers, reverse=True)
print(
    f'Your favorite teachers in reverse alphabetically order are: {sort_teachers}')

print(f'\nYour top two teachers are: {teachers[0]} and {teachers[1]}')
print(f'Your next two teachers are: {teachers[2]} and {teachers[3]}')
print(f'Your last favorite teacher is: {teachers[3]}')
print(f'You have a total of {len(teachers)} favorite teachers.')
