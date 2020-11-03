WHICH = 'NUM' # 'NUM' AND 'LETTER' ARE VALID


if WHICH == 'NUM':
    numbers = []

    for x in range(1,11):
        while True:
            inp = input(f'Enter number {str(x)}:')
            try:
                inp = int(inp)
                numbers.append(inp)
                break
            except ValueError:
                print('Thats not a number.')


    numbers = sorted(numbers)

    for index, num in enumerate(numbers):
        if index == len(numbers) - 1:
            print(num)
        else:
            print(f'{num}, ', end='')

else:
    letters = []
    s = input('Enter a string: ').lower().strip()
    for le in s:
        letters.append(le)

    letters = sorted(letters)
    for index, lett in enumerate(letters):
        if index == len(letters) - 1:
            print(lett)
        else:
            print(f'{lett}, ', end='')
