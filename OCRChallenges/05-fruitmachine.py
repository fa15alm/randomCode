from random import randint as rint
from math import floor


def roundthing(num):
    newnum = num * 10
    newnum = floor(newnum)
    return newnum / 10



fruits = ['Cherry', 'Bell', 'Lemon', 'Orange', 'Star', 'Skull']
credit = 1.0
while True:
    credit -= 0.2
    if credit < 0:
        print('You don\'t have enough money!')
        break
    slot1 = rint(0,5)
    slot2 = rint(0,5)
    slot3 = rint(0,5)
    print()
    print(fruits[slot1])
    print(fruits[slot2])
    print(fruits[slot3])
    print()
    if slot1 == 5 and slot2 == 5 and slot3 == 5:
        credit = 0
        print('You lost!')
        break
    elif (slot1 == 5 and slot2 == 5) or (slot1 == 5 and slot3 == 5) or (slot2 == 5 and slot3 == 5):
        credit -= 1
        print('You lost £1')
    elif slot1 == 1 and slot2 == slot1 and slot3 == slot1:
        credit += 5
        print('You got £5')
    elif slot1 == slot2 and slot2 == slot3:
        credit += 1
        print('You got £1')
    elif slot1 == slot2 or slot1 == slot3 or slot2 == slot3:
        credit += 0.5
        print('You got 50p')
    else:
        print('You got nothing')
    print('Credit: £' + str(roundthing(credit)) + '0')
    again = input('Do you want to play again? (Y/N): ').lower().strip()
    if again == 'y' or again == 'yes':
        continue
    else:
        print('Goodbye.')
        break
    
