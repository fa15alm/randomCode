import random
import os                                                                                          # Imports

deck = ['A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠', 
        'A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣',             # Defining the Deck of Cards
        'A♥', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥',
        'A♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦']

def getCard(deck):
    card = random.choice(deck)                                                              # Function to pick and ommit a random card from the deck
    deck.remove(card)                 
    return card

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

def main():
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
        print('Better luck next time!')
        return


    if calculateTotal(player) == 21 and len(player) == 2:                 # BLACKJACK
        os.system('cls')
        print('Your Hand: ' + player[0] + ', ' + player[1])
        print('Dealer\'s Hand: ' + dealer[0] + ', ' + dealer[1])
        if calculateTotal(dealer) == 21:
            print('You Draw!')
        else:
            print('You Win!')
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
                print('Dealer\'s Bust! You win!')
                break
            if calculateTotal(dealer) == 21:
                print('You Draw!')
                break
            elif calculateTotal(dealer) >= 17:
                print('Dealer stands on 17. You win!')
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
                print('Dealer\'s Bust! You win!')
                break
            if calculateTotal(dealer) == 21:
                print('You lost!')
                break
            elif calculateTotal(dealer) >= 17:
                print('Dealer stands on 17.')
                if calculateTotal(player) > calculateTotal(dealer):
                    print('You win!')
                elif calculateTotal(dealer) > calculateTotal(player):
                    print('You lost!')
                else:
                    print('You draw!')
                break
            else:
                cont = input('Dealer Hits. Press ENTER to continue.')
                dealer.append(getCard(deck))
        return
    
main()    
