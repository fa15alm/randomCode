import re
import bcrypt
import base64
from cryptography.fernet import Fernet
from random import choice, randint

with open('passwords.txt', 'r') as file:
    contents = file.read()
    masterpass = re.findall('MasterPassword: \'(.*)\'', contents)
    masterpass = bytes(masterpass[0], 'UTF-8')


def randomString(length):
    rs = []
    sc = [33, 35, 37, 42, 63, 94, 95]
    for x in range(length):
        cap = randint(65, 90)
        lower = randint(97, 122)
        num = randint(48, 57)
        special = choice(sc)
        which = randint(1, 4)
        if which == 1:
            rs.append(chr(cap))
        elif which == 2:
            rs.append(chr(lower))
        elif which == 3:
            rs.append(chr(num))
        elif which == 4:
            rs.append(chr(special))
    return ''.join(map(str, rs))


def menu():
    print('------------')
    print('q - Quit')
    print('n - New Password')
    print('d - Delete Existing Password')
    print('r - Retrieve Password')
    print('c - Change Master Password')
    print('------------')


def main(pswd):
    key = bytes(pswd, 'UTF-8')
    key_len = len(key)
    sen_len = str(key_len).encode('UTF-8')
    sen_len += b' ' * (32 - len(sen_len))
    key = base64.b64encode(sen_len)
    fkey = Fernet(key)
    global masterpass
    while True:
        menu()
        while True:
            with open('passwords.txt', 'r') as fl:
                contents = fl.read()
            choice = input()
            if choice.lower().strip() == 'q' or choice.lower().strip() == 'n' or choice.lower().strip() == 'r' or choice.lower().strip() == 'd' or choice.lower().strip() == 'c':
                break
            else:
                print('Please enter \'q\', \'n\', \'d\', \'r\', or \'c\'')
        if choice.lower().strip() == 'q':
            exit()
        elif choice.lower().strip() == 'n':
            pltfm = input('What platform will this password be used for? Type \'q\' to go back. ')
            pltfm = pltfm.lower().strip()
            if pltfm == 'q':
                continue
            with open('passwords.txt', 'a') as f:
                f.write('\n')
                pfmss = re.findall('Platform: \'(.*)\', Password:', contents)
                if pfmss.__contains__(pltfm):
                    print('There is already a password for that platform stored.')
                    continue
                passw = randomString(15)
                passw1 = bytes(passw, 'UTF-8')
                passw1 = fkey.encrypt(passw1)
                passw1 = str(passw1)
                passw1 = passw1.strip('b\'\'')
                f.write(f'Platform: \'{pltfm}\', Password: \'{passw1}\'')
            print(f'A password has been created for {pltfm}: {passw}')
        elif choice.lower().strip() == 'r':
            with open('passwords.txt', 'r') as fl:
                contents = fl.read()
                pltfrm = input(
                    'What platform do you want the password for? Type \'q\' to go back. Type \'l\' for a list of all '
                    'platforms. ')
                if pltfrm.lower().strip() == 'q':
                    continue
                elif pltfrm.lower().strip() == 'l':
                    pfms = re.findall('Platform: \'(.*)\', Password:', contents)
                    for p in pfms:
                        print(p)
                    continue
                pltfrm = pltfrm.lower().strip()
                platforms = re.findall('Platform: \'(.*)\', Password: ', contents)
                if platforms.__contains__(pltfrm):
                    pwds = re.findall(f'Platform: \'{pltfrm}\', Password: \'(.*)\'', contents)
                    password = pwds[0]
                    password = bytes(fkey.decrypt(bytes(password, 'UTF-8')))
                    password = str(password)
                    password = password.strip('b\'\'')
                    print(f'Your password for {pltfrm} is {password}')
                else:
                    print('You dont have a password stored for that platform.')
        elif choice.lower().strip() == 'c':
            while True:
                oldpass = input('Please enter the old password. Type \'q\' to go back. ')
                if oldpass.lower().strip() == 'q':
                    break
                if bcrypt.checkpw(bytes(oldpass, 'UTF-8'), masterpass):
                    newpass = bytes(input('Please now enter your new password. Type \'q\' to go back. '), 'UTF-8')
                    if newpass.lower().strip() == 'q':
                        break
                    newpass = bcrypt.hashpw(newpass, bcrypt.gensalt())
                    newpass = str(newpass)
                    newpass = newpass.strip('b\'\'')
                    cfl = open('passwords.txt', 'r')
                    lines = cfl.readlines()
                    lines[0] = f'MasterPassword: \'{newpass}\'\n'

                    cfl = open('passwords.txt', 'w')
                    cfl.writelines(lines)
                    cfl.close()
                    break
                else:
                    continue
        elif choice.lower().strip() == 'd':
            pf = input(
                'What is the name of the platform you want to delete? Type \'q\' to go back. Type \'l\' for a list of '
                'all platforms. ').lower().strip()
            pfs = re.findall('Platform: \'(.*)\', Password:', contents)
            if pf == 'q':
                continue
            elif pf == 'l':
                for p in pfs:
                    print(p)
                continue
            if pfs.__contains__(pf):
                print('Sorry, this feature is still in development.')
                continue
            else:
                print('You dont have a password stored for that platform.')


def loginThing():
    global masterpass
    print('Welcome to your Password Manager!')
    pw = str(input('Please enter your password - '))
    if bcrypt.checkpw(bytes(pw, 'UTF-8'), masterpass):
        main(pw)
    else:
        print('Wrong Password. Try Again.')
        loginThing()


loginThing()
