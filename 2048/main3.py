# ------------------------------------------- IMPORTS ------------------------------------------- #
import random
import pygame
import copy
import time

# ------------------------------------------ CONSTANTS ------------------------------------------ #

BOARD_WIDTH = 400
BOARD_HEIGHT = 400

UPPER_BORDER = 100
LOWER_BORDER = 50
SIDE_BORDERS = 50

ANIMATION_SPEED = 50

BORDER_WIDTH = 10

SQUARE_SIDE = (BOARD_HEIGHT-(BORDER_WIDTH*5))//4

SCREEN_WIDTH = BOARD_WIDTH+(SIDE_BORDERS*2)
SCREEN_HEIGHT = UPPER_BORDER+LOWER_BORDER+BOARD_HEIGHT

FPS = 60

TEXT_COLOUR = (119, 110, 101)

BORDER_COLOUR = (187, 173, 160)

BACKGROUND_COLOUR = (250, 250, 250)

BOARD_BACKGROUND_COLOUR = (205, 193, 180)

SQUARE_COLOUR = {0: BOARD_BACKGROUND_COLOUR, 2: (238, 228, 218), 4: (238, 225, 201), 8: (243, 178, 122), 
                 16: (246, 150, 100), 32: (247, 124, 95), 64: (247, 95, 59), 128: (237, 208, 115), 
                 256: (237, 204, 98), 512: (237, 198, 81), 1024: (238, 199, 68), 2048: (236, 194, 48), 
                 4096: (254, 61, 62), 8192: (255, 32, 33)}

# ------------------------------------------- GRAPHICS ------------------------------------------ #

def writeText(text, screen, x, y, colour=TEXT_COLOUR):
    t = font.render(text, True, colour)
    tRect = t.get_rect()
    tRect.center = (x, y)
    screen.blit(t, tRect)
    return tRect


def drawSquare(surface, x, y):
    pygame.draw.rect(surface, SQUARE_COLOUR[board[y][x] if board[y][x]<8192 else 8192], pygame.Rect(BORDER_WIDTH*(x+1)+(x*SQUARE_SIDE), BORDER_WIDTH*(y+1)+(y*SQUARE_SIDE), SQUARE_SIDE, SQUARE_SIDE), 0, 5)

        
def drawBorder(surface):
    pygame.draw.rect(surface, BORDER_COLOUR, pygame.Rect(0, 0, BOARD_WIDTH, BOARD_HEIGHT), 0, 5)

def drawBoard(surface):
    for x in range(4):
        for y in range(4):
            drawSquare(surface, x, y)
            if board[y][x] != 0:
                colour = (255, 255, 255)
                if board[y][x] in [2, 4]:
                    colour = TEXT_COLOUR
                writeText(str(board[y][x]), boardSurface, BORDER_WIDTH*(x+1)+(x*SQUARE_SIDE)+(SQUARE_SIDE//2), BORDER_WIDTH*(y+1)+(y*SQUARE_SIDE)+(SQUARE_SIDE//2), colour=colour)
    
def drawScreen(screen, boardSurface):
    screen.fill(BACKGROUND_COLOUR)
    boardSurface.fill(BACKGROUND_COLOUR)
    drawBorder(boardSurface)
    drawBoard(boardSurface)
    screen.blit(boardSurface, (SIDE_BORDERS, UPPER_BORDER))
    writeText('Score: ' + str(score), screen, SCREEN_WIDTH//2, UPPER_BORDER//2)

# ------------------------------------------ GAME SETUP ----------------------------------------- #
        
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
boardSurface = pygame.Surface((BOARD_WIDTH, BOARD_HEIGHT))
board = [[0 for i in range(4)]for i in range(4)]
font = pygame.font.Font('freesansbold.ttf', 32)
pygame.display.set_caption('2048')
score = 0
highScore = 0
running = True

def generateSquare(board):
    p = random.randint(1, 10)
    n = 4 if p == 1 else 2
    while True:
        x = random.randint(0, 3)
        y = random.randint(0, 3)
        if board[y][x] == 0:
            break
    board[y][x] = n
    
def moveSquares(direction, board):
    global score
    added = [[], [], [], []]
    t = 0
    while True:
        bCopy = copy.deepcopy(board)
        if direction == 'u':
            for x in range(0, 4):
                for y in range(1, 4):
                    if board[y-1][x] == 0:
                        board[y-1][x] = board[y][x]
                        board[y][x] = 0
                    if board[y-1][x] == board[y][x] and not(board[y-1][x] in added[x] or board[y][x] in added[x]):
                        board[y-1][x] = board[y][x]*2
                        score+=board[y][x]*2
                        board[y][x] = 0
                        added[x].append(board[y-1][x])
                        
        elif direction == 'd':
            for x in range(0, 4):
                for y in range(2, -1, -1):
                    if board[y+1][x] == 0:
                        board[y+1][x] = board[y][x]
                        board[y][x] = 0
                    if board[y+1][x] == board[y][x] and not(board[y+1][x] in added[x] or board[y][x] in added[x]):
                        board[y+1][x] = board[y][x]*2
                        score+=board[y][x]*2
                        board[y][x] = 0
                        added[x].append(board[y+1][x])
                
        elif direction == 'l':
            for y in range(0, 4):
                for x in range(1, 4):
                    if board[y][x-1] == 0:
                        board[y][x-1] = board[y][x]
                        board[y][x] = 0
                    if board[y][x-1] == board[y][x] and not(board[y][x-1] in added[y] or board[y][x] in added[y]):
                        board[y][x-1] = board[y][x]*2
                        score+=board[y][x]*2
                        board[y][x] = 0
                        added[y].append(board[y][x-1])
        elif direction == 'r':
            for y in range(0, 4):
                for x in range(2, -1, -1):
                    if board[y][x+1] == 0:
                        board[y][x+1] = board[y][x]
                        board[y][x] = 0
                    if board[y][x+1] == board[y][x] and not(board[y][x+1] in added[y] or board[y][x] in added[y]):
                        board[y][x+1] = board[y][x]*2
                        score+=board[y][x]*2
                        board[y][x] = 0
                        added[y].append(board[y][x+1])

        else:
            return False
        if board == bCopy:
            if t != 0 and not boardIsFull(board):
                generateSquare(board)
            break
        else:
            drawScreen(screen, boardSurface)
            pygame.display.update()
            time.sleep(1/ANIMATION_SPEED)
            t+=1

def boardIsFull(board):
    for x in range(4):
        for y in range(4):
            if board[y][x] == 0:
                return False
            if y<3:
                if board[y][x] == board[y+1][x]:
                    return False
            if y>0:
                if board[y][x] == board[y-1][x]:
                    return False
            if x<3:
                if board[y][x] == board[y][x+1]:
                    return False
            if x>0:
                if board[y][x] == board[y][x-1]:
                    return False

    return True


def resetGame():
    global board
    global score
    score = 0
    board = [[0 for i in range(4)]for i in range(4)]
    generateSquare(board)
    generateSquare(board)

    
# ------------------------------------------ MAIN LOOP ------------------------------------------ #

resetGame()
while running:
    clock.tick(FPS)
    drawScreen(screen, boardSurface)
    if boardIsFull(board):
        dim = pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT))
        dim.set_alpha(128)                
        dim.fill((180,180,180))           
        screen.blit(dim, (0,0))
        writeText('Game Over!', screen, SCREEN_WIDTH//2, SCREEN_HEIGHT//2-100, (255, 0, 0))
        pRect = writeText('Play Again', screen, SCREEN_WIDTH//2, SCREEN_HEIGHT//2+100, (0, 230, 200))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if pRect.collidepoint(event.pos):
                        resetGame()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    resetGame()
        if running:
            pygame.display.update()
        continue
    
    highScore = score if score>highScore else highScore

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                moveSquares('u', board)
            if event.key == pygame.K_DOWN:
                moveSquares('d', board)
            if event.key == pygame.K_LEFT:
                moveSquares('l', board)
            if event.key == pygame.K_RIGHT:
                moveSquares('r', board)
            if event.key == pygame.K_r:
                    resetGame()
    if running:
        pygame.display.update()
