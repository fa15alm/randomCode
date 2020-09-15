from random import randint

board = [' ' for x in range(10)]


def printBoard():  # Function to print the board out
    print(board[1], '|', board[2], '|', board[3])  # prints the 1st board line '  |   |  '
    print('--+---+--')  # prints the 2nd board line '--+---+--'
    print(board[4], '|', board[5], '|', board[6])  # prints the 3rd board line '  |   |  '
    print('--+---+--')  # prints the 4th board line '--+---+--'
    print(board[7], '|', board[8], '|', board[9])  # prints the 5th board line '  |   |  '


def insertLetter(letter, pos):  # Inserts a letter into the board
    board[pos] = letter


def isBlankSpace(pos):  # Checks if the space passed into the method is blank or not
    return board[pos] == ' '


def isWinner(letter, brd):  # Checks if the letter passed into the method has won
    return ((brd[1] == letter and brd[2] == letter and brd[3] == letter) or
            (brd[4] == letter and brd[5] == letter and brd[6] == letter) or
            (brd[7] == letter and brd[8] == letter and brd[9] == letter) or
            (brd[1] == letter and brd[4] == letter and brd[7] == letter) or
            (brd[2] == letter and brd[5] == letter and brd[8] == letter) or
            (brd[3] == letter and brd[6] == letter and brd[9] == letter) or
            (brd[1] == letter and brd[5] == letter and brd[9] == letter) or
            (brd[3] == letter and brd[5] == letter and brd[7] == letter))


def isBoardFull():  # Checks if the board is full
    return board.count(' ') == 1


def playerMove1():
    choice = input('Choose a space (1-9), You are Xs ')
    try:
        choice = int(choice)
        if 0 < choice < 10:
            if isBlankSpace(choice):
                insertLetter('X', choice)
            else:
                print('That space is occupied!')
                playerMove1()
        else:
            print('Please enter a number between 1 and 9!')
            playerMove1()
    except:
        print('Please enter a number between 1 and 9!')
        playerMove1()


def compMove():
    global board
    freeSpaces = []
    hasMadeMove = False
    
    for boardspace in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        if board[boardspace] == ' ':
            freeSpaces.append(boardspace)

    for space in freeSpaces:
        if not hasMadeMove:
            boardC = board.copy()
            boardC[space] = 'O'
            if isWinner('O', boardC):
                hasMadeMove = True
                insertLetter('O', space)
    if not hasMadeMove:
        for space in freeSpaces:
            if not hasMadeMove:
                boardC2 = board.copy()
                boardC2[space] = 'X'
                if isWinner('X', boardC2):
                    hasMadeMove = True
                    insertLetter('O', space)
    if not hasMadeMove:
        y = randint(0, len(freeSpaces) - 1)
        x = freeSpaces[y]
        insertLetter('O', x)


def main():
    print('TicTacToe!!')
    global board
    board = [' ' for x in range(10)]
    while not isBoardFull():
        if not isWinner('O', board):
            printBoard()
            playerMove1()
        else:
            printBoard()
            print('Haha! I won!')
            break
        if isBoardFull():
            break
        if not isWinner('X', board):
            printBoard()
            compMove()
            print()
        else:
            print('Well done player. You won!')
            break
    if isBoardFull():
        print('It\'s a tie!')


main()

while True:  # Play Again loop
    ans = input('Would you like to play again? (Y/N) - ')
    if ans.lower().strip() == 'y' or ans.lower().strip() == 'yes':
        board = [' ' for x in range(10)]
        main()
    elif ans.lower().strip() == 'n' or ans.lower().strip() == 'no':
        print('Thanks for playing!')
        break
    else:
        print('I SAID YES OR NO!')
