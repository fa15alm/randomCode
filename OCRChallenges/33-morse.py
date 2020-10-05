def makeMorse(string):
    string = string.lower().strip()
    morseify = {'a' : '.-', 'b' : '-...', 'c' : '-.-.', 'd' : '-..', 'e' : '.', 'f' : '..-.', 'g' : '--.', 'h' : '....', 'i' : '..', 'j' : '.---', 'k' : '-.-', 'l' : '.-..', 'm' : '--', 'n' : '-.', 'o' : '---', 'p' : '.--.', 'q' : '--.-', 'r' : '.-.', 's' : '...', 't' : '-', 'u' : '..-', 'v' : '...-', 'w' : '.--', 'x' : '-..-', 'y' : '-.--', 'z' : '--..', ' ' : '/', '.' : '.-.-.-', ',' : '--..--', '?' : '..--..'}
    output = []
    for letter in string:
        if morseify[letter]:
            output.append(morseify[letter])
            output.append(' ')
        else:
            output.append('?')
            output.append(' ')
    return ''.join(thing for thing in output)

def morseToText(string):
    output = []
    textify = {'.-' : 'a', '-...' : 'b', '-.-.' : 'c', '-..' : 'd', '.' : 'e', '..-.' : 'f', '--.' : 'g', '....' : 'h', '..' : 'i', '.---' : 'j', '-.-' : 'k', '.-..' : 'l', '--' : 'm', '-.' : 'n', '---' : 'o', '.--.' : 'p', '--.-' : 'q', '.-.' : 'r', '...' : 's', '-' : 't', '..-' : 'u', '...-' : 'v', '.--' : 'w', '-..-' : 'x', '-.--' : 'y', '--..' : 'z', '/' : ' ', '--..--' : ',', '.-.-.-' : '.', '..--..' : '?'}
    for char in string:
        if char not in ['.', '-', ' ', '/']:
            return 'ERROR: NOT MORSE'
    string = string.split()
    for word in string:
        output.append(textify[word])
    return ''.join(thing for thing in output)
