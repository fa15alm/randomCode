from random import randint

pw = 'lmao'

guess = ''

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while guess != pw:
    guess = ''
    for letter in range(len(pw)):
        guessLet = alphabet[randint(0, 25)]
        guess = guessLet + guess
    print(guess)

print(f'The password was \'{guess}\'.')
