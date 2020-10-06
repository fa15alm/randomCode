import re
def printMenu():
    print()
    print('----------------------')
    print('u - Use Dictionary')
    print('l - See Entries')
    print('c - Create Entry')
    print('q - Leave Program')
    print('----------------------')
    print()
while True:
    printMenu()
    choice = input('> ').strip().lower()
    if choice not in ['u', 'l', 'c', 'q']:
        print('That is not a valid option.')
        continue
    else:
        with open('textspeak.txt', 'r') as f:
            contents = f.read()
            ts = re.findall('\'(.*)\': \'', contents)
        if choice == 'q':
            print('Bye.')
            exit()
        elif choice == 'l':
            if len(ts) == 0:
                print('There are currently no entries.')
            else:
                for index, t in enumerate(ts):
                    if index == len(ts) - 1:
                        print(t)
                    else:
                        print(t + ', ', end='')
        elif choice == 'u':
            which = input('What entry would you like to see? Type q to leave. ').strip().lower()
            if which == 'q':
                continue
            else:
                if which in ts:
                    es = re.findall('\'' + which + '\': \'(.*)\'', contents)
                    print(which + ': ' + es[0])
                    continue
                else:
                    print('That entry does not exist. Type l for a list of entries.')
                    continue
        elif choice == 'c':
            with open('textspeak.txt', 'a') as f:
                entry = input('What\'s the text-speak of the phrase you want to store? Type q to quit. ').strip().lower()
                if entry in ts:
                    print('That is already an entry!')
                    continue
                else:
                    stored = input('What would you like that text-speak to store? ').strip()
                    print('Okay! All done! ' + entry + ': \'' + stored + '\'!')
                    with open('textspeak.txt', 'a') as f:
                        f.write('\'' + entry + '\': \'' + stored + '\'\n')
