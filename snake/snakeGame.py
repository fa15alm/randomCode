from random import randint as r
from os import system as sys
from time import sleep
import pygame

boardWidth = 17
boardHeight = 15
FPS = 10
MAXTICKSFORMOVE = 4

board = [[' ' for i in range(boardWidth)] for i in range(boardHeight)]

class Snake:
    def __init__(self):
        self.headColour = (97, 165, 65)
        self.bodyColour = (84, 211, 25)
        self.appleColour = (238, 55, 30)
        self.resetGame()
    def resetGame(self, apples=2):
        self.head = [7, 3]
        self.body = [[7, 2], [7, 1]]
        self.score = 0
        self.apples = []
        self.left = False
        self.right = True
        self.up = False
        self.down = False
        self.last = None
        for i in range(apples):
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

def writeText(text, screen, x, y, colour):
    t = font.render(text, True, colour)
    tRect = t.get_rect()
    tRect.center = (x, y)
    screen.blit(t, tRect)

moveQueue = []
moveTick = []
tickNum = 0
lose = False
paused = False
highScore = 0

while True:
    clock.tick(FPS)
    tickNum += 1
    pygame.display.set_caption('Snake Game        Score: ' + str(s.score))

    if paused:
        screen.fill((0, 0, 0))
        writeText('Game Paused.', screen, boardWidth*25, boardHeight*25-100, (0, 255, 255))
        writeText('Current Score: ' + str(s.score), screen, boardWidth*25, boardHeight*25, s.bodyColour)
        writeText('Press ESCAPE to unpause.', screen, boardWidth*25, boardHeight*25+100, (255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and pygame.key.name(event.key).upper() == 'ESCAPE':
                paused = False
        
        pygame.display.update()
        continue
    if not s.move():
        lose = True
        highScore = s.score if s.score>highScore else highScore
    if lose:
        screen.fill((0, 0, 0))
        writeText('Game Over!', screen, boardWidth*25, boardHeight*25-150, s.appleColour)
        writeText('Score: ' + str(s.score), screen, boardWidth*25, boardHeight*25-50, s.bodyColour)
        writeText('High Score: ' + str(highScore), screen, boardWidth*25, boardHeight*25+50, s.headColour)
        writeText('Press R to restart.', screen, boardWidth*25, boardHeight*25+150, (255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and pygame.key.name(event.key).upper() == 'ESCAPE'):
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and pygame.key.name(event.key).upper() == 'R':
                lose = False
                s.resetGame()
        
        pygame.display.update()
        continue

    if s.head in s.apples:
        s.grow()

    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            name = pygame.key.name(event.key).upper()
            if name == 'UP':
                moveQueue.append('u')
                moveTick.append(tickNum)
            if name == 'DOWN':
                moveQueue.append('d')
                moveTick.append(tickNum)
            if name == 'LEFT':
                moveQueue.append('l')
                moveTick.append(tickNum)
            if name == 'RIGHT':
                moveQueue.append('r')
                moveTick.append(tickNum)
            if name == 'ESCAPE':
                paused = True
            
    for index, t in enumerate(moveTick):
        if (tickNum-t)>MAXTICKSFORMOVE:
            moveQueue.pop(index)
            moveTick.pop(index)
    if moveQueue:
        s.setDirection(moveQueue.pop(0))
        moveTick.pop(0)
    
    
    screen.fill((0, 0, 0))
    for y in range(0, boardHeight):
        for x in range(0, boardWidth):
            if [y, x] in s.body:
                drawSquare(screen, x, y, s.bodyColour)
            if [y, x] in s.apples:
                drawSquare(screen, x, y, s.appleColour)
            if [y, x] == s.head:
                drawSquare(screen, x, y, s.headColour)

    pygame.display.update()
