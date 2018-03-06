num = int(input('enter a number:'))

for row in range(1, num + 1):
    for column in range (1, num + 1):
        print(row * column, end=' ')
    print('\n')
