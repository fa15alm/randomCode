import pygame, sys, copy, random



SCREEN_WIDTH = 510
SCREEN_HEIGHT = 510

BOX_WIDTH = SCREEN_WIDTH//3

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

X_COLOUR = (0, 0, 255)
O_COLOUR = (255, 0, 0)

LINE_WIDTH = 5


board = [[''for i in range(3)] for i in range(3)]

Xturn, Oturn = True, False

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('Tic Tac Toe!')
singlePlayer = True                                                  # SET TO FALSE TO PLAY WITH TWO PLAYERS

def changeTurn():
    global Xturn, Oturn
    Xturn = not Xturn
    Oturn = not Oturn


def drawX(x, y):
    startX = x*(SCREEN_WIDTH//3)+40
    startY = y*(SCREEN_HEIGHT//3)+40
    pygame.draw.line(screen, X_COLOUR, (startX, startY), (startX+BOX_WIDTH-80, startY+BOX_WIDTH-80), 10)
    pygame.draw.line(screen, X_COLOUR, (startX, startY+BOX_WIDTH-80), (startX+BOX_WIDTH-80, startY), 10)

def drawO(x, y):
    x *= SCREEN_WIDTH//3
    y *= SCREEN_HEIGHT//3
    pygame.draw.circle(screen, O_COLOUR, (x+BOX_WIDTH//2, y+BOX_WIDTH//2), 50, 10)


def drawBoxes():
    for y in range(3):
        for x in range(3):
            if board[y][x] == '':
                continue
            if board[y][x] == 'X':
                drawX(x, y)
            if board[y][x] == 'O':
                drawO(x, y)

def drawScreen(screen):
    screen.fill(BLACK)

    for i in range(2):
        pygame.draw.rect(screen, WHITE, pygame.Rect((SCREEN_WIDTH//3)*(i+1), 0, LINE_WIDTH, SCREEN_HEIGHT))
        pygame.draw.rect(screen, WHITE, pygame.Rect(0, (SCREEN_HEIGHT//3)*(i+1), SCREEN_WIDTH, LINE_WIDTH))
    
    drawBoxes()

    boxes = win('X') if win('X') else win('O')
    if boxes:
        startX, startY = boxes[0][0], boxes[0][1]
        endX, endY = boxes[2][0], boxes[2][1]
        pygame.draw.line(screen, WHITE, (startX*SCREEN_WIDTH//3+BOX_WIDTH//2, startY*SCREEN_WIDTH//3+BOX_WIDTH//2), (endX*SCREEN_WIDTH//3+BOX_WIDTH//2, endY*SCREEN_WIDTH//3+BOX_WIDTH//2), 30)

    pygame.display.update()



def win(letter, board=board):
    for i in range(3):
        if (board[i][0] == letter and board[i][1] == letter and board[i][2] == letter):
            return [(0, i), (1, i), (2, i)]
        if (board[0][i] == letter and board[1][i] == letter and board[2][i] == letter):
            return [(i, 0), (i, 1), (i, 2)]
    if (board[0][0] == letter and board[1][1] == letter and board[2][2] == letter):
        return [(0, 0), (1, 1), (2, 2)]
    if (board[2][0] == letter and board[1][1] == letter and board[0][2] == letter):
        return [(0, 2), (1, 1), (2, 0)]
    return False

def boardIsFull(board=board):
    for row in board:
        for item in row:
            if item == '':
                return False
    return True



def computerMove():
    global board
    freeSpaces = []
    for y, row in enumerate(board):
        for x, item in enumerate(row):
            if item == '':
                freeSpaces.append((x, y))
    
    for space in freeSpaces:
        b = copy.deepcopy(board)
        b[space[1]][space[0]] = 'O'
        if win('O', b):
            board[space[1]][space[0]] = 'O'
            return
    
    for space in freeSpaces:
        b = copy.deepcopy(board)
        b[space[1]][space[0]] = 'X'
        if win('X', b):
            board[space[1]][space[0]] = 'O'
            return
        
    space = random.choice(freeSpaces)
    board[space[1]][space[0]] = 'O'


while True:
    clock.tick()
    drawScreen(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if not singlePlayer or (singlePlayer and Xturn):
                    pos = event.pos
                    x = (pos[0])//(SCREEN_WIDTH//3)
                    y = (pos[1])//(SCREEN_HEIGHT//3)
                    if board[y][x] == '':
                        board[y][x] = 'O' if Oturn else 'X'
                        changeTurn()
                        continue

    if win('X'):
        while True:
            clock.tick()
            drawScreen(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    if win('O'):
        while True:
            clock.tick()
            drawScreen(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    
    if boardIsFull():
        while True:
            clock.tick()
            drawScreen(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    
    if Oturn and singlePlayer:
        computerMove()
        changeTurn()
