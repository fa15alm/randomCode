fib = [0, 1]
DIGITNUM = 1000
while True:
    fib.append(fib[len(fib) - 2] + fib[len(fib) - 1])
    possibleNum = str(fib[len(fib) - 1])
    if len(possibleNum) == DIGITNUM:
        print(len(fib) - 1)
        break
    else:
        continue
