from random import randint as r
from os import system as sys
import pygame

boardWidth = 17
boardHeight = 15
fps = 10
appleCountDefault = 2
appleCountMax = 100
fpsDefault = 10
fpsMax = 100
MAXTICKSFORMOVE = 4

board = [[' ' for i in range(boardWidth)] for i in range(boardHeight)]

class Snake:
    def __init__(self):
        self.headColour = (97, 120, 65)
        self.bodyColour = (84, 211, 25)
        self.appleColour = (238, 55, 30)
        self.highScore = 0
        self.appleCount = appleCountDefault
        self.resetGame()
    def resetGame(self):
        self.head = [7, 3]
        self.body = [[7, 2], [7, 1]]
        self.score = 0
        self.apples = []
        self.left = False
        self.right = True
        self.up = False
        self.down = False
        self.last = None
        for i in range(self.appleCount):
            self.genApple()
    def setDirection(self, dir):
        if (self.left and dir=='r') or (self.right and dir=='l') or (self.up and dir=='d') or (self.down and dir=='u'):
            return
        self.left = (True) if dir == 'l' else (False)
        self.right = (True) if dir == 'r' else (False)
        self.up = (True) if dir == 'u' else (False)
        self.down = (True) if dir == 'd' else (False)
    def move(self):
        x = self.head.copy()
        if self.left:
            self.head = ([x[0], x[1]-1]) 
        if self.right:
            self.head = ([x[0], x[1]+1]) 
        if self.up:
            self.head = ([x[0]-1, x[1]])
        if self.down:
            self.head = ([x[0]+1, x[1]])
        tbody = []
        for i in range(len(self.body)):
            if i == 0:
                tbody.append(x)
                continue
            tbody.append(self.body[i-1])
        if self.last:
            tbody.append(self.last)
            self.last = None
        self.body = tbody
        if self.head[0] < 0 or self.head[0] > boardHeight-1 or self.head[1] < 0 or self.head[1] > boardWidth-1 or s.head in s.body:
            return False
        return True
    
    def grow(self):
        self.apples.remove(self.head)
        self.genApple()
        self.last = self.body[-1]
        self.score += 1

    def genApple(self):
        while True:
            y, x = r(0,boardHeight-1), r(0, boardWidth-1)
            if [y, x] not in self.body and [y, x] != self.head and [y, x] not in self.apples:
                break
        self.apples.append([y, x])

def printGame():
    sys('cls')
    print('Score: ' + str(s.score))
    for y in range(boardHeight):
        for x in range(boardWidth):
            if [y, x] == s.head:
                print('O', end=' ')
                continue
            if [y, x] in s.body:
                print('.', end=' ')
                continue
            if [y, x] in s.apples:
                print('A', end=' ')
                continue
            print(' ', end=' ')
        print()


s = Snake()


pygame.init()
screen = pygame.display.set_mode((boardWidth*50, boardHeight*50))
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 32)

def drawSquare(screen, x, y, colour, width=50, height=50):
    pygame.draw.rect(screen, colour, pygame.Rect((x*width), (y*height), width, height))
    for i in range(4):
        pygame.draw.rect(screen, (255,255,255), ((x*width)-i,(y*height)-i,width+2,height+2), 1)

def writeText(text, screen, x, y, colour):
    t = font.render(text, True, colour)
    tRect = t.get_rect()
    tRect.center = (x, y)
    screen.blit(t, tRect)
    return tRect



def gameOver():
    while True:
        screen.fill((0, 0, 0))
        writeText('Game Over!', screen, boardWidth*25, boardHeight*25-150, s.appleColour)
        writeText('Score: ' + str(s.score), screen, boardWidth*25, boardHeight*25-50, s.bodyColour)
        writeText('High Score: ' + str(s.highScore), screen, boardWidth*25, boardHeight*25+50, s.headColour)
        writeText('Press R to restart.', screen, boardWidth*25, boardHeight*25+150, (255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and pygame.key.name(event.key).upper() == 'R':
                s.resetGame()
                pressToPlay()
                return
            if event.type == pygame.KEYDOWN and pygame.key.name(event.key).upper() == 'ESCAPE':
                startMenu()
        
        pygame.display.update()

def drawGame():
    screen.fill((0, 0, 0))
    for y in range(0, boardHeight):
        for x in range(0, boardWidth):
            if [y, x] in s.body:
                drawSquare(screen, x, y, s.bodyColour)
            if [y, x] in s.apples:
                drawSquare(screen, x, y, s.appleColour)
            if [y, x] == s.head:
                drawSquare(screen, x, y, s.headColour)

def pauseScreen():
    while True:
        drawGame()
        writeText('Game Paused.', screen, boardWidth*25, boardHeight*25-100, (0, 255, 255))
        writeText('Current Score: ' + str(s.score), screen, boardWidth*25, boardHeight*25, s.bodyColour)
        writeText('Press P to unpause.', screen, boardWidth*25, boardHeight*25+100, (255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and pygame.key.name(event.key).upper() == 'ESCAPE':
                startMenu()
            if event.type == pygame.KEYDOWN and pygame.key.name(event.key).upper() == 'P':
                return
            
        
        pygame.display.update()

def pressToPlay():
    while True:
        drawGame()
        writeText('Press any key to begin.', screen, boardWidth*25, boardHeight*25, (255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                return
        pygame.display.update()

def startMenu():
    pygame.display.set_caption('Snake Game')
    while True:
        screen.fill((0, 0, 0))
        writeText('Snake Game', screen, boardWidth*25, 150, s.bodyColour)
        pRect = writeText('Play', screen, boardWidth*25, boardHeight*25-100, (255, 255, 255))
        hRect = writeText('Help', screen, boardWidth*25, boardHeight*25, (255, 255, 255))
        oRect = writeText('Options', screen, boardWidth*25, boardHeight*25+100, (255, 255, 255))
        qRect = writeText('Quit', screen, boardWidth*25, boardHeight*25+250, (255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if qRect.collidepoint(event.pos):
                        pygame.quit()
                        quit()
                    if pRect.collidepoint(event.pos):
                        s.resetGame()
                        playGame()
                        return
                    if hRect.collidepoint(event.pos):
                        helpScreen()
                    if oRect.collidepoint(event.pos):
                        optionsScreen()
                    

        pygame.display.update()

def helpScreen():
    while True:
        screen.fill((0, 0, 0))
        writeText('Welcome to Snake.', screen, boardWidth*25, 100, (255, 255, 255))
        writeText('Snake is a game where you control a snake', screen, boardWidth*25, 250, (255, 255, 255))
        writeText('and collect apples which make your snake grow.', screen, boardWidth*25, 300, (255, 255, 255))
        writeText('The larger your snake, the higher score you', screen, boardWidth*25, 400, (255, 255, 255))
        writeText('will achieve.', screen, boardWidth*25, 450, (255, 255, 255))
        writeText('Good Luck!', screen, boardWidth*25, 550, (255, 255, 255))
        bRect = writeText('Back', screen, boardWidth*25, 700, s.appleColour)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if bRect.collidepoint(event.pos):
                        return

        pygame.display.update()

def optionsScreen():
    global fps
    while True:
        screen.fill((0, 0, 0))
        writeText('OPTIONS', screen, boardWidth*25, 50, (255, 255, 255))
        writeText('Number of Apples', screen, boardWidth*25, 200, (255, 255, 255))
        lessApples = writeText('-', screen, boardWidth*25-100, 250, s.appleColour)
        writeText(str(s.appleCount), screen, boardWidth*25, 250, (255, 255, 255))
        moreApples = writeText('+', screen, boardWidth*25+100, 250, s.bodyColour)

        writeText('Snake Speed', screen, boardWidth*25, 350, (255, 255, 255))
        lessSpeed = writeText('-', screen, boardWidth*25-100, 400, s.appleColour)
        writeText(str(fps), screen, boardWidth*25, 400, (255, 255, 255))
        moreSpeed = writeText('+', screen, boardWidth*25+100, 400, s.bodyColour)

        rRect = writeText('Reset', screen, boardWidth*25, 125, s.appleColour)

        bRect = writeText('Back', screen, boardWidth*25, 700, s.appleColour)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if lessApples.collidepoint(event.pos):
                        s.appleCount = s.appleCount-1 if s.appleCount>1 else 1
                    if moreApples.collidepoint(event.pos):
                        s.appleCount = s.appleCount+1 if s.appleCount<appleCountMax else s.appleCount
                    if lessSpeed.collidepoint(event.pos):
                        fps = fps-1 if fps>1 else 1
                    if moreSpeed.collidepoint(event.pos):
                        fps = fps+1 if fps<fpsMax else fps
                    if rRect.collidepoint(event.pos):
                        fps = fpsDefault
                        s.appleCount = appleCountDefault
                    if bRect.collidepoint(event.pos):
                        return

        pygame.display.update()

def playGame():
    moveQueue = []
    moveTick = []
    tickNum = 0
    pressToPlay()
    while True:
        clock.tick(fps)
        tickNum += 1
        pygame.display.set_caption('Snake Game        Score: ' + str(s.score))

        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                name = pygame.key.name(event.key).upper()
                if name in ['UP', 'W']:
                    moveQueue.append('u')
                    moveTick.append(tickNum)
                if name in ['DOWN', 'S']:
                    moveQueue.append('d')
                    moveTick.append(tickNum)
                if name in ['LEFT', 'A']:
                    moveQueue.append('l')
                    moveTick.append(tickNum)
                if name in ['RIGHT', 'D']:
                    moveQueue.append('r')
                    moveTick.append(tickNum)
                if name == 'ESCAPE':
                    startMenu()
                if name == 'P':
                    pauseScreen()
                
        for index, t in enumerate(moveTick):
            if (tickNum-t)>MAXTICKSFORMOVE:
                moveQueue.pop(index)
                moveTick.pop(index)
        if moveQueue:
            s.setDirection(moveQueue.pop(0))
            moveTick.pop(0)

        if not s.move():
            s.highScore = s.score if s.score>s.highScore else s.highScore
            gameOver()

        if s.head in s.apples:
            s.grow()

        drawGame()


        pygame.display.update()


startMenu()
