from random import randint, choice
def randomString(length):
    rs = []
    sc = [33, 35, 37, 42, 63, 94, 95]
    for x in range(length):
        cap = randint(65, 90)
        lower = randint(97, 122)
        num = randint(48, 57)
        special = choice(sc)
        which = randint(1, 4)
        if which == 1:
            rs.append(chr(cap))
        elif which == 2:
            rs.append(chr(lower))
        elif which == 3:
            rs.append(chr(num))
        elif which == 4:
            rs.append(chr(special))
    return ''.join(map(str, rs))
