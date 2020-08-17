import time, os, sys
from zones import *
from questions import *

def titleScreen():
    title = True
    play = False
    help_ = False
    options = False
    with open('title.txt') as title:
        cntnts = title.read()
        os.system('cls')
    print(cntnts)

prompt = '> '
output = ''

name = 'Gregory'
job = 'Warrior'

choice = ''
menuChoices = ['play', 'help', 'options', 'quit']

title = True
play = False
help_ = False
options = False

#=======================================================================# Write Function

def write(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

#=======================================================================# Setup Game Function

def setupGame(name, job):
    write('Hello. What is your name?')
    name = input(prompt)
    write('What job would you like?')
    write('You can play as Mage, Warrior, or Priest.')
    joblist = ['mage', 'warrior', 'priest']
    job = input(prompt).lower().strip()
    while not job in joblist:
        write('That is not a valid Job.')
        job = input(prompt).lower().strip()
    write(f'Welcome, {name} the {job}!')
    write(f'Are you ready to play?')
    while True:
        ready = input(prompt).lower().strip()
        if ready == 'y' or ready == 'yes':
            write('Cool! Let\'s go!')
            break
        elif ready == 'n' or ready == 'no':
            write('Ok. Just play again when you\'re ready!')
            time.sleep(1)
            main()
            break
        else:
            write('I do not understand that answer.')

#=======================================================================# Classes

class Player(object):
    def __init__(self):
        self.name = 'bob'
        self.job = 'warrior'
        self.health = 50
        self.location = 'a2'
    def move(self):
        write('Where would you like to move to? ')
        where = input()
        print()
        if where in ['up', 'north']:
            if ZONEMAP[player.location][UP] == 'none':
                write('I cannot go anymore in that direction.')
            else:
                player.location = ZONEMAP[player.location][UP]
                printLocation()
        elif where in ['down', 'south']:
            if ZONEMAP[player.location][DOWN] == 'none':
                write('I cannot go anymore in that direction.')
            else:
                player.location = ZONEMAP[player.location][DOWN]
                printLocation()
        elif where in ['left', 'west']:
            if ZONEMAP[player.location][LEFT] == 'none':
                write('I cannot go anymore in that direction.')
            else:
                player.location = ZONEMAP[player.location][LEFT]
                printLocation()
        elif where in ['right', 'east']:
            if ZONEMAP[player.location][RIGHT] == 'none':
                write('I cannot go anymore in that direction.')
            else:
                player.location = ZONEMAP[player.location][RIGHT]
                printLocation()
        else:
            write('I do not know where that is.')

player = Player()

#=======================================================================# Get Choice Function

def getChoice():
    global choice
    while True:
        choice = input(prompt).strip().lower()
        if not choice in menuChoices:
            print('Please enter a correct choice. ')
            continue
        else:
            break

#=======================================================================# Do Correct Thing Function

def doCorrectThing():
    if choice == 'play':
        play()
    elif choice == 'options':
        options()
    elif choice == 'help':
        help_()
    elif choice == 'quit':
        quit_()
    else:
        getChoice()
        doCorrectThing()

#=======================================================================# Play Function

def play():
    play = True
    title = False
    options = False
    help_ = False
    setupGame(name, job)
    player.name = name
    player.job = job
    printLocation()
    while True:
        doPrompt()

#=======================================================================# Options Menu

def options():
    play = False
    title = False
    options = True
    help_ = False
    pass

#=======================================================================# Help Menu

def help_():
    play = False
    title = False
    options = False
    help_ = True
    pass

#=======================================================================# Quit Function

def quit_():
    play = False
    title = False
    options = False
    help_ = False
    print('k bye')
    time.sleep(0.5)
    exit()

#=======================================================================# Main Function

def main():
    titleScreen()
    getChoice()
    doCorrectThing()

#=======================================================================# MAP

"""
PLAYER STARTS AT A2

+-----------+
|a1|a2|a3|a4|
|--+--+--+--|
|b1|b2|b3|b4|
|--+--+--+--|
|c1|c2|c3|c4|
|--+--+--+--|
|d1|d2|d3|d4|
+-----------+
"""

#=======================================================================# Print Location Function

def printLocation():
    os.system('cls')
    print('----------------------------')
    write(f'- {ZONEMAP[player.location][ZONENAME]}')
    write(f'- {ZONEMAP[player.location][DESCRIPTION]}')
    write('- You have already solved this zone.' if ZONEMAP[player.location][SOLVED] == True else '- You have not solved this zone.')
    print('----------------------------')

def doPrompt():
    print('\n=====================================')
    write('What would you like to do?')
    action = input(prompt).lower()
    acceptable_actions = ['move', 'go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'look']
    while action not in acceptable_actions:
        write('Unknown action, Try again.\n')
        action = input(prompt).lower()
    if action == 'quit':
        quit_()
    elif action in ['move', 'go', 'travel', 'walk']:
        player.move()
    elif action in ['examine', 'inspect', 'interact', 'look']:
        write(f'You examine: {ZONEMAP[player.location][EXAMINATION]}')
        if ZONEMAP[player.location][HASQUESTION]:
            if ZONEMAP[player.location][SOLVED] == True:
                write('You have already solved this puzzle.')
            else:
                write(QUESTIONS[player.location]['Q'])
                answer = input(prompt).lower().strip()
                if answer == QUESTIONS[player.location]['A']:
                    write('You got it correct!')
                    ZONEMAP[player.location][SOLVED] = True
                else:
                    write('You got it wrong.') 

main()