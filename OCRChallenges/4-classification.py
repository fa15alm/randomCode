# Sea - Whale, Dolphin, Seal, Penguin, Octopus, Squid

    # 8 Tentacles: Octopus, Squid
        # One Eye: Squid
    # Feet: Penguin
    # Live On Land: Seal
    # Is it big: Whale
        # otherwise dolphin

# Land - Horse, Cow, Sheep, Pig, Dog, Cat, Lion, Tiger, Ostrich, Sparrow, Spider, Ant, Bee, Wasp, Termite

    # Insect: Spider, Ant, Bee, Wasp, Termite
        # Fly: Bee, Wasp
            # Die on sting: Bee
        # 6 legs: ant, termite
            # Narrow Waist: ant
        # else: spider
    # 4 Legs: Horse, Cow, Sheep, Pig, Dog, Cat, Lion, Tiger
        # Household pet: Cat, Dog
            # Feline: Cat
        # Big Cat: Lion, Tiger
            # males have manes: Lion
        # Ride them: Horse
        # Produce Milk : Cow
        # Wool: Sheep
        # else Pig
    # else: Sparrow, Ostrich

print('I will show you a series of Yes No questions. (Y/N)')

sea = input('Does your animal swim? ').lower().strip()
if sea == 'yes' or sea == 'y':
    tent8 = input('Does your animal have 8 tentacles? ').lower().strip()

    if tent8 == 'yes' or tent8 == 'y':
        eye = input('Does your animal have 1 eye? ').lower().strip()
        if eye == 'yes' or eye == 'y':
            print('Your animal was a squid!')
        elif eye == 'no' or eye == 'n':
            print('Your animal was an octopus!')

    elif tent8 == 'no' or tent8 == 'n':
        feet = input('Does your animal have feet? ').lower().strip()
        if feet == 'yes' or feet == 'y':
            print('Your animal was a penguin!')
        elif feet == 'no' or feet == 'n':
            land = input('Does yor animal occasionally go onto land/rocks? ').lower().strip()
            if land == 'yes' or land == 'y':
                print('Your animal was a seal!')
            elif land == 'no' or land == 'n':
                big = input('Is your animal big? ').lower().strip()
                if big == 'yes' or big == 'y':
                    print('Your animal was a whale!')
                elif big == 'no' or big == 'n':
                    print('Your animal was a dolphin!')


elif sea == 'no' or sea == 'n':
    insect = input('Is your animal an insect? ').lower().strip()
    if insect == 'yes' or insect == 'y':
        fly = input('Does your animal fly? ').lower().strip()
        if fly == 'yes' or fly == 'y':
            dos = input('Does your animal die upon stinging? ').lower().strip()
            if dos == 'yes' or dos == 'y':
                print('Your animal was a bee!')
            elif dos == 'no' or dos == 'n':
                print('Your animal was a wasp!')
        elif fly == 'no' or fly == 'n':
            leg6 = input('Does your animal have 6 legs? ').lower().strip()
            if leg6 == 'yes' or leg6 == 'y':
                narrow = input('Does your insect have a narrow waist? ').lower().strip()
                if narrow == 'yes' or narrow == 'y':
                    print('Your animal was an ant!')
                elif narrow == 'no' or narrow == 'n':
                    print('Your animal was a termite!')
            elif leg6 == 'no' or leg6 == 'n':
                print('Your animal was a spider!')
    elif insect == 'no' or insect == 'n':
        leg4 = input('Does your animal have 4 legs? ').lower().strip()
        if leg4 == 'yes' or leg4 == 'y':
            hp = input('Is your animal a household pet? ').lower().strip()
            if hp == 'yes' or hp == 'y':
                feline = input('Is your animal a feline? ').lower().strip()
                if feline == 'yes' or feline == 'y':
                    print('Your animal was a cat!')
                elif feline == 'no' or feline == 'n'
                    print('Your animal was a dog!')
            elif hp == 'no' or hp == 'n':
                bigcat = input('Is your animal a big cat? ').lower().strip()
                if bigcat == 'yes' or bigcat == 'y':
                    mane = input('Do males of your animal have manes? ').lower().strip()
                    if mane == 'yes' or mane == 'y':
                        print('Your animal was a lion!')
                    elif mane == 'no' or mane == 'n':
                        print('Your animal was a tiger!')
                elif bigcat == 'no' or bigcat == 'n':
                    ride = input('Do people ride your animal? ').lower().strip()
                    if ride == 'yes' or ride == 'y':
                        print('Your animal was a horse!')
                    elif ride == 'no' or ride == 'n':
                        milk = input('Does your animal produce milk? ').lower().strip()
                        if milk == 'yes' or milk == 'y':
                            print('Your animal was a cow!')
                        elif milk == 'no' or milk == 'n':
                            wool = input('Does your animal grow wool? ').lower().strip()
                            if wool == 'yes' or wool == 'y':
                                print('Your animal was a sheep!')
                            elif wool == 'no' or wool == 'n':
                                print('Your animal was a pig!')
        elif leg4 == 'no' or leg4 == 'n':
            bird = input('Can your animal fly? ').lower().strip()
            if bird == 'yes' or bird == 'y':
                print('Your animal was a sparrow!')
            elif bird == 'no' or bird == 'n':
                print('Your animal was an ostrich!')
