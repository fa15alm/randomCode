def isPanagram(string):
    string = string.lower()
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for letter in string:
        try:
            alphabet.pop(alphabet.index(letter))
            continue
        except:
            continue
    if len(alphabet) == 0:
        return True
    else:
        return False
