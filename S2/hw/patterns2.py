num = int(input('enter a number: '))

for i in range(1, num):
    if i % 2 == 0:
        print(1, end=' ')
    else:
        print (0, end=' ')    
print('\n')
