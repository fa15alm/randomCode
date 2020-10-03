from random import choice

fruit = ['cherry', 'bell', 'lemon', 'orange', 'star', 'skull']

class Player:
    def __init__(self, name, money=1.0):
        self.name = name
        self.money = money

name = input('What is your name? ').strip()
p = Player(name)

while True:
    print('Your Money: £' + str(p.money))
    enter = input('Press enter to spin! (Cost 20p), type STOP to walk away.')
    if enter.lower().strip() == 'stop':
        print('You walked away with £' + str(p.money))
        break
    slot1 = choice(fruit)
    slot2 = choice(fruit)
    slot3 = choice(fruit)
    print()
    print(slot1)
    print(slot2)
    print(slot3)
    print()
    if (slot1 == slot2 and slot2 != slot3) or (slot2 == slot3 and slot2 != slot1) or (slot1 == slot3 and slot1 != slot2):
        print('You won £0.50')
        p.money += 0.50
    elif slot1 == slot2 and slot2 == slot3:
        print('You won £1')
        p.money += 1
    elif slot1 == 'bell' and slot2 == 'bell' and slot3 == 'bell':
        print('You won £5')
        p.money += 5
    elif (slot1 == 'skull' and slot2 == 'skull' and slot3 != 'skull') or (slot1 == 'skull' and slot3 == 'skull' and slot2 != 'skull') or (slot2 == 'skull' and slot3 == 'skull' and slot1 != 'skull'):
        print('You lost £1')
        p.money -= 1
    elif slot1 == 'skull' and slot2 == 'skull' and slot3 == 'skull':
        print('You lost all your money (' + str(p.money) + ')!')
        p.money = 0
    if p.money <= 0:
        print('You lost all your money!')
        break
en = input('Press enter to close the program.')
