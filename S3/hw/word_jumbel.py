from random import *
from getpass import getpass

quizz = getpass('enter your quizz: ')
char = list(quizz)
shuffle(char)
print(*char)

key = input('enter your awnser: ')
if key == quizz:
    print('Bingo!!')
else:
    print(':(')
