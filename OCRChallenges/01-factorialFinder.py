def find_factorial(number):
    result = 1
    for x in range(1, number + 1):
        result *= x
    return str(result)

while True:
    num = input('Enter a number to find the factorial of: ')
    try:
        num = int(num)
        if num < 0:
            print('Please enter a positive integer.')
            continue
        else:
            break
    except ValueError:
        print('Please enter a positive integer.')
        continue

print('The factorial of is ' + find_factorial(num))
