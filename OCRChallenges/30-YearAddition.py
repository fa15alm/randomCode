
while True:
    year = input('year: ')
    try:
        year = int(year)
        if len(str(year)) == 4:
            year = str(year)
            break
        else:
            print('Enter a 4 digit year please.')
    except ValueError:
        print('thats not a year.')

result = 0
for num in year:
    result += int(num)

print(result)
