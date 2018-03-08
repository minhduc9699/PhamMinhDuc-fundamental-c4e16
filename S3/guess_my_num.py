from random import randint

num = randint(0,100)

playing = True
count = 0
while playing:
    guess = int(input('yout guess? '))

    if guess > num:
        print('little too large')
    elif guess < num:
        print('Too small')
    else:
        print('Bingo')
        break
    count += 1
    if count == 7:
        print('you lose :(' )
        playing = False
