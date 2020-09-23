def fib(number):
    fibarray = []
    fibarray.append(0)
    fibarray.append(1)
    for x in range(1, number - 1):
        fibarray.append(fibarray[x - 1] + fibarray[x])
    return fibarray

while True:
    amount = input('How many places of the Fibonacci sequence would you like? (minimum 2) ').strip()
    try:
        amount = int(amount)
        if amount < 2:
            print('Please enter a number greater than 2.')
            continue
        else:
            break
    except ValueError:
        print('Please enter a number.')

fibarray = fib(amount)
for index, fib in enumerate(fibarray):
    if index == len(fibarray) - 1:
        print(str(fib))
    else:
        print(str(fib) + ', ', end='')
