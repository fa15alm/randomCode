print('I will reverse some text of yours.')
text = input('Enter some text: ').strip()


def reverseText(string):
    return string[::-1]

print(reverseText(text))
