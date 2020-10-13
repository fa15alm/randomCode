print('I will check if a string is a palindrome.')
text = input('Enter some text: ').strip().lower()


def reverseText(string):
    return string[::-1]

if reverseText(text) == text:
    print('It is a palindrome.')
else:
    print('It is not a palindrome.')
