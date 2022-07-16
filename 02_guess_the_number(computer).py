# computer selects a number and user guesses it

import random

print("\nPlease enter lower limit and higher limit...")

low_num = int(input('Enter lower limit: '))
high_num = int(input('Enter higher limit: '))


if low_num > high_num:
    # higher limit can't be less than lower limit
    print("\nLearn some math please.And restart the game...\n")
    exit()

comp = random.randint(low_num , high_num)

print(f"\nComputer has selected a number between {low_num} and {high_num}. Your task is to guess that number\n")

user_guess = low_num - 1        # Initialized user guessed number (out of limit) just to enter into following loop
count = 0

while user_guess != comp:
    user_guess = int(input("Guess a number: "))
    count += 1
    
    if user_guess == comp:
        print(f'\nUser has guessed computer selected number {comp} in {count} turns. Well Done.\n')
    
    elif user_guess < comp:
        print('Low guess, try again...\n')
    
    elif user_guess > comp:
        print('High guess, try again...\n')