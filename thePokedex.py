
from pokedex import pokedex

#===================================================================================# VARIABLES

pokedex = pokedex.Pokedex()
totalPokemon = pokedex.get_pokemon_counts()['total']

#===================================================================================# FUNCTIONS


def menu():
    print()
    print('+-----------------------------------------+')
    print('|   ____       _            _             |')
    print('|  |  __ \    | |          | |            |')
    print('|  | |__) |__ | | _____  __| | _____  __  |')
    print('|  |  ___/ _ \| |/ / _ \/ _` |/ _ \ \/ /  |')
    print('|  | |  | (_) |   <  __/ (_| |  __/>  <   |')
    print('|  |_|   \___/|_|\_\___|\__,_|\___/_/\_\  |')
    print('|                                         |')
    print('+-----------------------------------------+')
    print()
    inp = input('Name/Number > ')
    print()
    if inp.strip().lower() == 'q':
        print('Goodbye!')
        enter = input('Press ENTER to close the pokedex.')
        exit()
    elif inp.strip() == '':
        print('That is not a valid pokemon name or number.')
        menu()
    elif inp.isdigit():
        if int(inp) < 1 or int(inp) > totalPokemon:
            print(f'That is an invalid number. There are only {str(totalPokemon)} pokemon.')
            menu()
        else:
            main([1, int(inp)])
    else:
        main([0, inp.lower()])


def printPokemon(p):
    p = p[0]

    number = p['number']
    name = p['name']
    species = p['species']
    types = p['types']
    nAbilities = p['abilities']['normal']
    hAbilities = p['abilities']['hidden']
    eggGroups = p['eggGroups']

    gender = p['gender']

    height = p['height']
    weight = p['weight']

    fam = p['family']
    evoStage = fam['evolutionStage']
    evoLine = fam['evolutionLine']

    starter = p['starter']
    legendary = p['legendary']
    mythical = p['mythical']
    ultraBeast = p['ultraBeast']
    mega = p['mega']

    gen = p['gen']

    description = p['description']


    print(f'----------------------------------------')
    print(f' Name: {name}                           ')
    print(f' Number: {str(number)}                  ')
    if gen:
        print(f' Generation: {str(gen)}             ')
    print(f' Species: {species}                     ')
    
    print(f' Types: ', end="")
    for index, t in enumerate(types):
        if index == len(types) - 1:
            print(t)
        else:
            print(t + ', ', end="")

    print()
    
    if nAbilities:      
        print(f' Normal Abilities: ', end="")
        for index, a in enumerate(nAbilities):
            if index == len(nAbilities) - 1:
                print(a)
            else:
                print(a + ', ', end="")
                
    if hAbilities:
        print(f' Hidden Abilities: ', end="")
        for index, a in enumerate(hAbilities):
            if index == len(hAbilities) - 1:
                print(a)
            else:
                print(a + ', ', end="")

    print()
    
    if eggGroups:
        print(f' Egg Groups: ', end="")
        for index, a in enumerate(eggGroups):
            if index == len(eggGroups) - 1:
                print(a)
            else:
                print(a + ', ', end="")
    if gender:
        print(f' Gender: {str(gender[0])}% Male, {str(gender[1])}% Female')

    print(f' Height: {height}                       ')
    print(f' Weight: {weight}                       ')
    print()

    if fam:
        print()
        if evoStage:
            print(f' Evolution Stage: {str(evoStage)} ')
        if evoLine:
            print(f' Evolution Line: ', end="")
            for index, a in enumerate(evoLine):
                if index == len(evoLine) - 1:
                    print(a)
                else:
                    print(a + ', ', end="")
        print()

    if starter:
        print(' Starter: True     ')
    if legendary:
        print(' Legendary: True    ')
    if mythical:
        print(' Mythical: True      ')
    if ultraBeast:
        print(' UltraBeast: True    ')
    if mega:
        print(' Mega: True     ')

    
    if description:
        print()
        print(f' Description: {description}')
        
    print(f'----------------------------------------')
    

def main(out):
    if out[0] == 0: # Input was a String
        name = out[1]
        try:
            pokemon = pokedex.get_pokemon_by_name(name)
            printPokemon(pokemon)
            enter = input('Press ENTER to continue!')
            menu()
        except KeyError:
            print('That is not a Pokemon!')
            enter = input('Press ENTER to continue!')
            menu()
        
    else: # Input was not a String
        num = out[1]
        pokemon = pokedex.get_pokemon_by_number(num)
        printPokemon(pokemon)
        enter = input('Press ENTER to continue!')
        menu()




menu()
