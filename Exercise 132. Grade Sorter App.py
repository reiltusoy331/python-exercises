print('=== Welcome To Grade Sorter App ===')

grades = []
grade1 = int(input('What is your first grade (0-100): '))
grades.append(grade1)
grade2 = int(input('What is your second grade (0-100): '))
grades.append(grade2)
grade3 = int(input('What is your third grade (0-100): '))
grades.append(grade3)
grade4 = int(input('What is your fourth grade (0-100): '))
grades.append(grade4)


print(f"\nYour grades are: {grades}")

sorted_grades = sorted(grades, reverse=True)
print(f"\nYour grades from highest to lowest are: {sorted_grades}")

print(f"\nThe lowest two grades will now be dropped.")
print(f"Removed grade:{sorted_grades.pop()}")
print(f"Removed grade:{sorted_grades.pop()}")

print(f"\nYour remaining grades are: {sorted_grades}")
print(f"Nice work! Your highest grade is a {sorted_grades[0]}.")
