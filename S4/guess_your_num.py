from random import randint

low = 0
mid = 50
high = 101
print('Guess your number game')
input('now think of a number from 0 to 100, then press Enter')
print('press C if my number is correct')
print('press S if my number is smaller than yours')
print('press L if my number is larger than your')

while True:
    answer = input('is {0} your number? '.format(mid)).upper()

    if answer == 'S':
        low = mid
        mid = ((low + high) // 2)
    elif answer == 'L':
        high = mid
        mid = ((low + high) // 2)
    elif answer == 'C':
        print('i knew it')
        break
