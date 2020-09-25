import random
import time
import sys

def isEven(num):
    numd = num / 2
    numid = num // 2
    if numd == numid:
        return True
    else:
        return False

def write(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
    def roll(self, amount):
        while True:
            result = random.randint(1, amount)
            if result == 1:
                continue
            else:
                break
        self.score += result
        if isEven(result):
            self.score += 10
        else:
            self.score -= 5
        return str(result)

p1name = input('What is your name, Player one? ')
write('Hello, ' + p1name)
p1 = Player(p1name)

p2name = input('What is your name, Player two? ')
write('Hello, ' + p2name)
p2 = Player(p2name)

rtp = input('Ready to play? (Press Enter) ')

for x in range(1, 6):
    p1roll = p1.roll(12)
    write(p1.name + ' rolled a total of ' + p1roll)
    time.sleep(0.5)
    p2roll = p2.roll(12)
    write(p2.name + ' rolled a total of ' + p2roll)

print()
print(p1.name + '\'s score was ' + str(p1.score))
print(p2.name + '\'s score was ' + str(p2.score))
print()
if p1.score > p2.score:
    print(p1.name + ' won!')
elif p2.score > p1.score:
    print(p2.name + ' won!')
else:
    print('It was a draw!')
