from random import randint as r
from os import system as sys
from time import sleep

boardWidth = 17
boardHeight = 15
FPS = 5

board = [[' ' for i in range(boardWidth)] for i in range(boardHeight)]

class Snake:
    def __init__(self):
        self.head = [7, 3]
        self.body = [[7, 2], [7, 1]]
        self.score = 0
        self.apples = []
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.last = None
    def setDirection(self, dir):
        self.left = (True) if dir == 'Left' else (False)
        self.right = (True) if dir == 'Right' else (False)
        self.up = (True) if dir == 'Up' else (False)
        self.down = (True) if dir == 'Down' else (False)
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

    def onKeyPress(self, e):
        dir = e.keysym
        self.setDirection(dir)

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
s.setDirection('Right')
#printGame()
#x = input('Press enter to start.')
s.genApple()

printGame()

while True:
    sleep(1/FPS)
    printGame()
    # check keypress
    if not s.move():
        break
    if s.head in s.apples:
        s.grow()

print('You crashed!')
print('Your final score was', s.score)
