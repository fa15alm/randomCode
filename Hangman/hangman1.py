from random import randint

#=================================================================================================# Variables

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

stage = {0 : '     +-----\n     |     \n     |     \n     |     \n     |     \n-----|-----',
         1 : '     +--+--\n     |  |  \n     |  O  \n     |     \n     |     \n-----|-----',
         2 : '     +--+--\n     |  |  \n     |  O  \n     |  |  \n     |     \n-----|-----',
         3 : '     +--+--\n     |  |  \n     |  O  \n     | /|  \n     |     \n-----|-----',
         4 : '     +--+--\n     |  |  \n     |  O  \n     | /|\ \n     |     \n-----|-----',
         5 : '     +--+--\n     |  |  \n     |  O  \n     | /|\ \n     | /   \n-----|-----',
         6 : '     +--+--\n     |  |  \n     |  O  \n     | /|\ \n     | / \ \n-----|-----'}

stageNum = 0
guessedLets = []

with open('mywords.txt', 'r', encoding='utf8') as f:
    lines = f.readlines()
    lineAmount = len(lines) - 1

#=================================================================================================# Functions

def printInfo(word):
    print()
    print('--------------------------------------------------------------------------')
    print()
    print(stage[stageNum])
    print()
    display_word = "".join(char if char in guessedLets else "_" for char in word)
    print(f'Word ({str(len(display_word))}): {display_word}')
    print('Guessed Letters: ', end='')
    for index, letter in enumerate(guessedLets):
        if index < len(guessedLets) - 1:
            print(letter + ', ', end='')
        else:
            print(letter + '', end='')
    print()

def main():
    global word
    global wordArray
    global stageNum
    global guessedLets
    stageNum = 0
    guessedLets = []
    wordArray = []
    #==============================================#
    while True:
        lineNumber = randint(0, lineAmount)
        word = lines[lineNumber].lower().strip()
        if len(word) < 6:
            continue
        for lettr in word:
            if not alphabet.__contains__(lettr):
                continue
        else:
            break

    for let in word:
        wordArray.append(let)
    #==============================================#

    while True:
        printInfo(word)
        while True:
            guess = input('Make a guess: ').lower().strip()
            if len(guess) > 1:
                print('Please enter a single letter.')
            elif not alphabet.__contains__(guess):
                print('Please enter a single letter. ')
            elif guessedLets.__contains__(guess):
                print('You have already guessed that letter!')
            else:
                break
        guessedLets.append(guess)
        if not wordArray.__contains__(guess):
            stageNum += 1
        display_word = "".join(char if char in guessedLets else "_" for char in word)
        if display_word == word:
            print('You won! The word was \'' + word + '\'')
            break
        if stageNum == 7:
            print('You lost! The word was \'' + word + '\'')
            break

#=================================================================================================# Rest of code

main()

while True:
    yn = input('Would you like to play again? (Y/N) ').lower().strip()
    if yn == 'y' or yn == 'yes':
        main()
        continue
    elif yn == 'n' or yn == 'no':
        print('Thanks for playing!')
        break
    else:
        print('Please enter either Y or N.')
        continue

exit()
