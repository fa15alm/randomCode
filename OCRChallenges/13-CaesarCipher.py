def cipher(string, key):
    result = []
    string = string.lower()
    for letter in string:
        letnum = ord(letter)
        letnum += key
        if letnum > 122:
            letnum -= 122
            letnum += 96
        let = chr(letnum)
        result.append(let)
    return ''.join(letter for letter in result)

def decipher(string, key):
    result = []
    string = string.lower()
    for letter in string:
        letnum = ord(letter)
        letnum -= key
        if letnum < 97:
            letnum += 122
            letnum -= 96
        let = chr(letnum)
        result.append(let)
    return ''.join(letter for letter in result)
