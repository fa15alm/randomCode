board = [' ' for x in range(10)]


def printBoard():  # Function to print the board out
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])


def insertLetter(letter, pos):  # Inserts a letter into the board
    board[pos] = letter


def isBlankSpace(pos):  # Checks if the space passed into the method is blank or not
    return board[pos] == ' '


def isWinner(letter):  # Checks if the letter passed into the method has won
    return ((board[1] == letter and board[2] == letter and board[3] == letter) or
            (board[4] == letter and board[5] == letter and board[6] == letter) or
            (board[7] == letter and board[8] == letter and board[9] == letter) or
            (board[1] == letter and board[4] == letter and board[7] == letter) or
            (board[2] == letter and board[5] == letter and board[8] == letter) or
            (board[3] == letter and board[6] == letter and board[9] == letter) or
            (board[1] == letter and board[5] == letter and board[9] == letter) or
            (board[3] == letter and board[5] == letter and board[7] == letter))


def isBoardFull():  # Checks if the board is full
    return board.count(' ') == 1


def playerMove1():
    run = True
    while run:
        pos = input('Enter a space 1-9. You are Xs  ')
        try:
            pos = int(pos)
            if 0 < pos < 10:
                if isBlankSpace(pos):
                    insertLetter('X', pos)
                    run = False
                else:
                    print('Please enter an unoccupied space!')
            else:
                print('Please enter a number between 1-9!')
        except:
            print('Please type a number between 1 and 9!')


def playerMove2():
    run = True
    while run:
        pos = input('Enter a space 1-9. You are Os ')
        try:
            pos = int(pos)
            if 0 < pos < 10:
                if isBlankSpace(pos):
                    insertLetter('O', pos)
                    run = False
                else:
                    print('Please enter an unoccupied space!')
            else:
                print('Please enter a number between 1-9!')
        except:
            print('Please type a number between 1 and 9!')


def main():
    print('TicTacToe!')
    printBoard()
    while not isBoardFull():
        if not (isWinner('O')):
            playerMove1()
            printBoard()
        else:
            print('Congrationlations Player 2 (O), You win!')
            break
        if isBoardFull():
            break
        if not (isWinner('X')):
            playerMove2()
            printBoard()
        else:
            print('Congratulations Player 1 (X), You win!')
            break
    if isBoardFull():
        print('Its a tie!')


main()

while True:
    answer = input('Would you like to play again? (Y/N)')
    if answer.lower() == 'y' or answer.lower() == 'yes':
        board = [' ' for x in range(10)]
        main()
    if answer.lower() == 'n' or answer.lower() == 'no':
        print('Thanks for playing, See you next time!')
        break
