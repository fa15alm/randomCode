import random
import os                                                                                          # Imports




class Player:
    def __init__(self, startingCredits=100):
        self.credits = startingCredits
    def give(self, credits):
        self.credits += credits
    def take(self, credits):
        self.credits -= credits


p = Player()

deck = ['A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠', 
        'A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣',             # Defining the Deck of Cards
        'A♥', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥',
        'A♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦']

def getCard(deck):
    card = random.choice(deck)                                                              # Function to pick and ommit a random card from the deck
    deck.remove(card)                 
    return card

def resetDeck(deck):
    deck = ['A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠', 
        'A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣',           
        'A♥', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥',
        'A♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦']

def calculateTotal(cards):
    total = 0
    aces = 0
    for card in cards:
        if card[0] == 'A':
            aces += 1
        elif card[0] in ['1', 'J', 'Q', 'K']:
            total += 10
        else:
            total += int(card[0])
    for i in range(0, aces):
        if total + 11 > 21:
            total += 1
        else:
            total += 11
    return total

def main(bet, p):
    dealer = []
    player = []

    dealer.append(getCard(deck))
    player.append(getCard(deck))
    dealer.append(getCard(deck))
    player.append(getCard(deck))

    while True:                           # PLAYER'S TURNS
        os.system('cls')
        print('Dealer\'s Hand: ' + dealer[0] + ', ??')


        print('Your Hand: ', end='')
        for index, card in enumerate(player):
            if index == len(player) - 1:
                print(player[index])
            else:
                print(player[index], end=', ')

        # CALCULATIONS 
        if calculateTotal(player) == 21 and len(player) == 2:
            print('Blackjack, Nice!')
            break
        if calculateTotal(player) == 21:
            print('21, Nice!')
            break
        if calculateTotal(player) > 21:
            print('Oops! You\'re Bust!')
            break



        choice = input('Hit or Stand? ').strip().lower()
        if choice in ['h', 'hit']:
            player.append(getCard(deck))
        else:
            break
    

    cont = input('Press ENTER to continue.')

    # DEALER STUFF

    if calculateTotal(player) > 21:                              # PLAYER BUST
        os.system('cls')
        print('Dealer\'s Hand: ', end='')
        for index, card in enumerate(dealer):
            if index == len(dealer) - 1:
                print(dealer[index])
            else:
                print(dealer[index], end=', ')

        print('Your Hand: ', end='')
        for index, card in enumerate(player):
            if index == len(player) - 1:
                print(player[index])
            else:
                print(player[index], end=', ')
        print('Better luck next time! You lost ' + str(bet) + ' credits.')
        p.take(bet)
        return


    if calculateTotal(player) == 21 and len(player) == 2:                 # BLACKJACK
        os.system('cls')
        print('Dealer\'s Hand: ' + dealer[0] + ', ' + dealer[1])
        print('Your Hand: ' + player[0] + ', ' + player[1])
        if calculateTotal(dealer) == 21:
            print('You Draw!')
        else:
            print('You Win ' + str(bet * 1.5) + ' credits!')
            p.give(bet * 1.5)
        return


    if calculateTotal(player) == 21:                                   # 21
        while True:
            os.system('cls')
            print('Dealer\'s Hand: ', end='')
            for index, card in enumerate(dealer):
                if index == len(dealer) - 1:
                    print(dealer[index])
                else:
                    print(dealer[index], end=', ')

            print('Your Hand: ', end='')
            for index, card in enumerate(player):
                if index == len(player) - 1:
                    print(player[index])
                else:
                    print(player[index], end=', ')
            
            if calculateTotal(dealer) > 21:
                print('Dealer\'s Bust! You win ' + str(bet) + ' credits!')
                p.give(bet)
                break
            if calculateTotal(dealer) == 21:
                print('You Draw!')
                break
            elif calculateTotal(dealer) >= 17:
                print('Dealer stands on 17. You win ' + str(bet) + ' credits!')
                p.give(bet)
                break
            else:
                cont = input('Dealer Hits. Press ENTER to continue.')
                dealer.append(getCard(deck))
        return
    
    else:                                                                     # PLAYER STOOD
        while True:
            os.system('cls')
            print('Dealer\'s Hand: ', end='')
            for index, card in enumerate(dealer):
                if index == len(dealer) - 1:
                    print(dealer[index])
                else:
                    print(dealer[index], end=', ')

            print('Your Hand: ', end='')
            for index, card in enumerate(player):
                if index == len(player) - 1:
                    print(player[index])
                else:
                    print(player[index], end=', ')
            
            if calculateTotal(dealer) > 21:
                print('Dealer\'s Bust! You win ' + str(bet) + ' credits!')
                p.give(bet)
                break
            if calculateTotal(dealer) == 21:
                print('You lost ' + str(bet) + ' credits!')
                p.take(bet)
                break
            elif calculateTotal(dealer) >= 17:
                print('Dealer stands on 17.')
                if calculateTotal(player) > calculateTotal(dealer):
                    print('You win ' + str(bet) + ' credits!')
                    p.give(bet)
                elif calculateTotal(dealer) > calculateTotal(player):
                    print('You lost ' + str(bet) + ' credits!')
                    p.take(bet)
                else:
                    print('You draw!')
                break
            else:
                cont = input('Dealer Hits. Press ENTER to continue.')
                dealer.append(getCard(deck))
        return
    

def menu():
    os.system('cls')
    print('==============================')
    print('Welcome to Blackjack!')
    print()
    print('1 - Play')
    print('2 - Settings')
    print('3 - Quit')
    print()
    print('Your Credits: ' + str(p.credits))
    print('==============================')
    choice = 0
    while choice not in ['1', '2', '3']:
        choice = input('> ')
    return choice

while True:
    resetDeck(deck)
    c = menu()
    if c == '3':
        enter = input('Goodbye! Press ENTER to continue.')
        break
    elif c == '2':
        os.system('cls')
        while True:
            newCredits = input('What would you like to set your credits to? ')
            try:
                newCredits = int(newCredits)
                p.credits = newCredits
                break
            except ValueError:
                print('That is not a number.')
                continue
    while True:
        print('Your Credits: ' + str(p.credits))
        bet = int(input('What\'s your bet? '))
        if (bet % 2) != 0:
            print('The bet must be an even number.')
            continue
        break
    main(bet, p)
    enter = input('Press ENTER to continue.')
