import random
import time
import sys
import re

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

# p1name = input('What is your name, Player one? ')
# write('Hello, ' + p1name)
# p1 = Player(p1name)

# p2name = input('What is your name, Player two? ')
# write('Hello, ' + p2name)
# p2 = Player(p2name)

with open('passwords.txt', 'r') as nf:
    contents = nf.read()
    names = re.findall('Name: \'(.*)\', Password:', contents)


# AUTHENTICATING PLAYER 1

while True:
    p1name = input('What is your name, Player one? ').strip()
    if names.__contains__(p1name.lower()):
        break
    else:
        write('That name is not a registered name. Try again.')
        continue

while True:
    p1pass = input('What is your password, ' + p1name + '? ').strip()
    if p1pass.lower() == 'quit':
        exit()
    passwords = re.findall('Name: \'' + p1name.lower() + '\', Password: \'(.*)\'', contents)
    if passwords[0] == p1pass:
        write('Welcome, ' + p1name + ', You have been granted access.')
        p1 = Player(p1name)
        break
    else:
        write('That is not your password. Try again or type \'quit\' to close the program.')
        continue


# AUTHENTICATING PLAYER 2

while True:
    p2name = input('What is your name, Player two? ').strip()
    if p1name.lower() == p2name.lower():
        write('That is player one\'s name!')
        continue
    elif names.__contains__(p2name.lower()):
        break
    else:
        write('That name is not a registered name. Try again.')
        continue

while True:
    p2pass = input('What is your password, ' + p2name + '? ').strip()
    if p2pass.lower() == 'quit':
        exit()
    passwords = re.findall('Name: \'' + p2name.lower() + '\', Password: \'(.*)\'', contents)
    if passwords[0] == p2pass:
        write('Welcome, ' + p2name + ', You have been granted access.')
        p2 = Player(p2name)
        break
    else:
        write('That is not your password. Try again or type \'quit\' to close the program.')
        continue

rtp = input('Ready to play? (Press Enter) ')

for x in range(1, 6):
    p1roll = p1.roll(12)
    write(p1.name + ' rolled a total of ' + p1roll)
    time.sleep(0.5)
    p2roll = p2.roll(12)
    write(p2.name + ' rolled a total of ' + p2roll)
    time.sleep(0.5)

print()
print(p1.name + '\'s score was ' + str(p1.score))
print(p2.name + '\'s score was ' + str(p2.score))
print()
if p1.score > p2.score:
    print(p1.name + ' won!')
    with open('champs.txt', 'a') as f:
        f.write(p1.name + ' won against ' + p2.name + ' with ' + str(p1.score) + ' points!\n')
elif p2.score > p1.score:
    print(p2.name + ' won!')
    with open('champs.txt', 'a') as f:
        f.write(p2.name + ' won against ' + p1.name + ' with ' + str(p2.score) + ' points!\n')
else:
    print('It was a draw!')
