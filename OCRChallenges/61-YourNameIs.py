name = input('What is your name? ').strip()
age = input('What is your age? ').strip()
form = input('What is your form? ').strip()
with open(name + '-' + age + '-' + form + '.txt', 'a') as f:
    f.write('Your name is ' + name + ', you are ' + age + ' years old, and you are in form ' + form + '.')
print('Your name is ' + name + ', you are ' + age + ' years old, and you are in form ' + form + '.')
