print('===Welcome to the Letter Counter App===')

name = input('What is your name: ').strip()
print(f"Hello {name.title()}!")

print("I will count the number of time that specific letter occurs in a message.")

message = input("Please enter a message: ")
letter = input("Which letter would you like to count the occurrences of: ")

count_letter = message.count(letter)
print(f"{name.title()}, your message has {count_letter} {letter}'s in it.")
