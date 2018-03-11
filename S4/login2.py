from getpass import *

tai_khoan = 'c4e'
password = 'codethechange'

count = 0
logging = True
while logging:
    print('hi there, this is a superuser gateway')
    user_name = input('Username: ')
    if user_name == tai_khoan:
        pass_input = getpass('password')
        if pass_input == password:
            print('welcome')
            break
        else:
            print('password is incorrect')
    else:
        print('Username is incorrect')
    count += 1
    if count == 3:
        print('you failed to login 3 times, go away')
        break
