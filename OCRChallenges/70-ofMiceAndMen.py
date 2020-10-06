import os
import random

number = random.randint(1000,9999)
numarray = []
guessarray = []
mice = 0
men = 0
number = str(number)
for num in number:
    numarray.append(num)

os.system('cls')
while True:
    guess = input('What is your guess of the number? ').strip()
    os.system('cls')
    try:
        guess = int(guess)
        if guess < 1000 or guess > 9999:
            print('Please enter a 4 digit number.')
            continue
        else:
            guess = str(guess)
            guessarray = []
            for g in guess:
                guessarray.append(g)
            for index, gu in enumerate(guessarray):
                if gu == numarray[index]:
                    mice += 1
                else:
                    men += 1
            if mice == 4:
                print('You got the number, ' + str(number) + '!')
                break
            else:
                print('You got ' + str(mice) + ' mice and ' + str(men) + ' men with ' + str(guess) + '.')
                mice = 0
                men = 0
    except ValueError:
        print('Please specifically enter a number.')
    
