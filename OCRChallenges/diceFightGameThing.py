from random import randint
from math import floor as roundDown
from time import sleep
import re

class Player:
    def __init__(self, name):
        self.name = name
        self.strength = 10
        self.skill = 10
        self.dead = False
    def roll(self, sides):
        return randint(1, sides)    
    # def initAttr(self):
    #     roll12 = self.roll(12)
    #     roll4 = self.roll(4)
    #     rolltotal = roll12 // roll4
    #     self.strength += rolltotal
    #     roll12 = self.roll(12)
    #     roll4 = self.roll(4)
    #     rolltotal = roll12 // roll4
    #     self.skill += rolltotal
while True:
    di = input('Would you like to use the scoreboard, Or use the game? (s/g) ').lower().strip()
    if di in ['s', 'g']:
        break
    else:
        print('That is not a valid option.')
        continue

if di == 's':
    with open('attributes.txt', 'r') as f:
        contents = f.read()
    names = re.findall('\'(.*)\':', contents)
    nm = input('Whose attributes do u wanna pull? ').strip().lower()
    if nm in names:
        strength = re.findall('\'' + nm + '\': Strength: \'(.*)\', Skill: ', contents)
        skill = re.findall('\', Skill: \'(.*)\'', contents)
        for i in range(0, len(strength)):
            print(nm + '\'s Strength is ' + strength[i] + ', and their Skill is ' + skill[i])
        exit()
    else:
        print('That player is not on the scoreboard.')
        exit()

p1name = input('Player 1, What is your name? ').strip()
p2name = input('Player 2, What is your name? ').strip()
p1 = Player(p1name)
p2 = Player(p2name)
p1.strength = int(input('What should ' + p1name + '\'s strength be set to? ').strip())
p1.skill = int(input('What should ' + p1name + '\'s skill be set to? ').strip())
p2.strength = int(input('What should ' + p2name + '\'s strength be set to? ').strip())
p2.skill = int(input('What should ' + p2name + '\'s skill be set to? ').strip())


# STRENGTH MOD
if p1.strength > p2.strength:
    strengthDif = p1.strength - p2.strength
elif p1.strength < p2.strength:
    strengthDif = p2.strength - p1.strength
else:
    strengthDif = 0

strengthDif /= 5
strengthMod = roundDown(strengthDif)
print('Stength Mod - ' + str(strengthMod))

# SKILL MOD
if p1.skill > p2.skill:
    skillDif = p1.skill - p2.skill
elif p1.skill < p2.skill:
    skillDif = p2.skill - p1.skill
else:
    skillDif = 0

skillDif /= 5
skillMod = roundDown(skillDif)
print('Skill Mod - ' + str(skillMod))

print('It is time to throw dice, ' + p1.name + ', You are first.')
enter = input('Press enter to see your roll. ')
p1roll = p1.roll(6)
print(p1.name + ' rolled a ' + str(p1roll))
sleep(0.5)
print(p2.name + ', It is your turn now.')
enter = input('Press enter to see your roll. ')
p2roll = p2.roll(6)
print(p2.name + ' rolled a ' + str(p2roll))

if p1roll > p2roll:
    p1.skill += skillMod
    p1.strength += strengthMod
    p2.skill -= skillMod
    p2.strength -= strengthMod
elif p1roll < p2roll:
    p2.skill += skillMod
    p2.strength += strengthMod
    p1.skill -= skillMod
    p1.strength -= strengthMod

if p1.strength < 0:
    p1.dead = True
if p1.skill < 0:
    p1.skill = 0
if p2.strength < 0:
    p2.dead = True
if p2.skill < 0:
    p2.skill = 0

print(p1.name + '\'s Skill, Strength: ' + str(p1.skill) + ', ' + str(p1.strength))
print(p2.name + '\'s Skill, Strength: ' + str(p2.skill) + ', ' + str(p2.strength))

if p1.dead:
    print(p1.name + ' Died.')
    exit()
elif p2.dead:
    print(p2.name + ' Died.')
    exit()
else:
    print('No one died.')

with open('attributes.txt', 'a') as f:
    f.write('\'' + p1.name.lower() + '\': Strength: \'' + str(p1.strength) + '\', Skill: \'' + str(p1.skill) + '\'\n')
    f.write('\'' + p2.name.lower() + '\': Strength: \'' + str(p2.strength) + '\', Skill: \'' + str(p2.skill) + '\'\n')
