def orGate(input1, input2):
    if input1 == 1:
        return 1
    if input2 == 1:
        return 1
    if input1 == 0 and input2 == 0:
        return 0
def andGate(input1, input2):
    if input1 == 1 and input2 == 1:
        return 1
    else:
        return 0
def xorGate(input1, input2):
    if input1 == 1 and input2 == 0:
        return 1
    if input2 == 1 and input1 == 0:
        return 1
    else:
        return 0
def nandGate(input1, input2):
    if input1 == 1 and input2 == 1:
        return 0
    else:
        return 1
def norGate(input1, input2):
    if input1 == 0 and input2 == 0:
        return 1
    else:
        return 0
gates = ['or', 'and', 'xor', 'nand', 'nor']
while True:
    gate = input('What gate should I use? (OR, AND, XOR, NAND, NOR) ').lower().strip()
    if gate not in gates:
        print('Enter a valid gate.')
        continue
    else:
        break
while True:
    input1 = input('Input1: ').strip()
    try:
        input1 = int(input1)
        if input1 == 1 or input1 == 0:
            break
        else:
            print('Enter 1 or 0.')
    except ValueError:
        print('Enter 1 or 0.')
while True:
    input2 = input('Input2: ').strip()
    try:
        input2 = int(input2)
        if input2 == 1 or input2 == 0:
            break
        else:
            print('Enter 1 or 0.')
    except ValueError:
        print('Enter 1 or 0.')

if gate == 'or':
    print(orGate(input1, input2))
elif gate == 'and':
    print(andGate(input1, input2))
elif gate == 'xor':
    print(xorGate(input1, input2))
elif gate == 'nand':
    print(nandGate(input1, input2))
elif gate == 'nor':
    print(norGate(input1, input2))
