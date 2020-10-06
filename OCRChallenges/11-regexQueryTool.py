import re

string = input('Please enter a string: ').strip()
pattern = input('Please enter a regex pattern: ')
results = re.findall(pattern, string)
if len(results) == 0:
    print('I could not find a match in your string.')
else:
    for index, result in enumerate(results):
        if index == len(results) - 1:
            print(result)
        else:
            print(result + ', ', end='')
