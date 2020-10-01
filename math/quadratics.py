import time
from math import sqrt

CALCULATINGTIME = True

print('My Quadratic Solver!')
time.sleep(0.5)

while True:
    a = input('What is a? ').strip()
    try:
        a = int(a)
        break
    except ValueError:
        print('An Integer, please.')
        continue

while True:
    b = input('What is b? ').strip()
    try:
        b = int(b)
        break
    except ValueError:
        print('An Integer, please.')
        continue

while True:
    c = input('What is c? ').strip()
    try:
        c = int(c)
        break
    except ValueError:
        print('An Integer, please.')
        continue

ans1 = (-b + sqrt((b ** 2) - (4 * a * c))) / (2 * a)
ans2 = (-b - sqrt((b ** 2) - (4 * a * c))) / (2 * a)

if CALCULATINGTIME:
    print('Calculating...')
    time.sleep(0.7)

print('x = ' + str(ans1))
print('or')
print('x = ' + str(ans2))
