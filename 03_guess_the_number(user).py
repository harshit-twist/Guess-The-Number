# User selects a number and computer guesses it

import random

print("\nPlease enter lower limit and higher limit...")

low_num = int(input('Enter lower limit: '))
high_num = int(input('Enter higher limit: '))


if low_num > high_num:
    # higher limit can't be less than lower limit
    print("\nLearn some math please.And restart the game...\n")
    exit()


user = int(input(f"Choose a number between {low_num} and {high_num}: "))


if user < low_num or user > high_num:
    print("What a choice. Can't u even read English correctly. Restart game kiddo...\n")
    exit()

count = 0


while True:
    comp_guess = random.randint(low_num,high_num)

    x = input(f'\nComputer guesses {comp_guess}. Is it correct(c), low(l) or high(h): ')
    count += 1

    if (comp_guess == user) and (x == 'h' or x == 'l'):
        print("\nNow you are cheating. I don't want to play. Bye...\n")
        break

    elif x == 'c':
        print(f'\n*** Computer correctly guessed user selected number {user} in {count} turns. ***\n')
        break
    
    elif x == 'l':
        print('Dumb machine, you guessed low, select again')
        low_num = comp_guess + 1
    
    elif x == 'h':
        print('Dumb machine, you guessed high, select again')
        high_num = comp_guess - 1
    
    else:
        print("Invalid response.")
        count -= 1