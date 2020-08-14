from time import sleep
import random


def rockPaperScissors():
    choice1 = input('Rock Paper or Scissors? ')
    choice = choice1.lower()
    botchoice = random.randint(1, 3)
    if botchoice == 1:
        bot = 'Rock'
    if botchoice == 2:
        bot = 'Paper'
    if botchoice == 3:
        bot = 'Scissors'
    if choice == 'r' or choice == 'rock':
        print('I chose %s!' % bot)
        if botchoice == 1:
            return print('Its a draw!')
        if botchoice == 2:
            return print('I win!')
        if botchoice == 3:
            return print('You Win!')
    if choice == 'p' or choice == 'paper':
        print('I chose %s!' % bot)
        if botchoice == 1:
            return print('You Win!')
        if botchoice == 2:
            return print('Its a draw!')
        if botchoice == 3:
            return print('I win!')
    if choice == 's' or choice == 'scissors':
        print('I chose %s!' % bot)
        if botchoice == 1:
            return print('I win!')
        if botchoice == 2:
            return print('You Win!')
        if botchoice == 3:
            return print('Its a draw!')
    else:
        print('Please enter Rock, Paper, or Scissors!')
        rockPaperScissors()


rockPaperScissors()
while True:
    answer = input('Would you like to play again? (Y/N)')
    if answer.lower() == 'y' or answer.lower() == 'yes':
        rockPaperScissors()
    if answer.lower() == 'n' or answer.lower() == 'no':
        print('Thanks for playing, see you again next time!')
        exit()
    else:
        continue
