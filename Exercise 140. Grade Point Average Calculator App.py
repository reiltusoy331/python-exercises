print('\t\t\t=== Grade Point Average Calculator App ===')

student = input('What is your name: ').title()
number_grades = int(input('How many grades would you like to enter: '))

grades = []
for num in range(1, number_grades+1):
    grade = int(input(f'Enter grade {num}: '))
    grades.append(grade)

print('\nGrades Highest to Lowest: ')
sort_grades = sorted(grades, reverse=True)
for sort_grade in sort_grades:
    print(f'\t {sort_grade}')

avg = sum(sort_grades)/len(sort_grades)

print(f'\n{student}\'s Grade Summary:')
print(f'\t Total Number of Grades: {len(sort_grades)}')
print(f'\t Highest Grade: {max(sort_grades)}')
print(f'\t Lowest Grade: {min(sort_grades)}')
print(f'\t Average: {avg}')

desired_avg = int(input('\nWhat is your desired average: '))

print(f'\nGood luck {student}!')
