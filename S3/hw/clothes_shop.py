stuff = ['T-shirt', 'Sweater']

def Creat():
    stuff_add = input('Enter new stuff: ')
    stuff.append(stuff_add)
    Read()

def Read():
    print('Our items: ')
    for index, item in enumerate(stuff):
        print(index + 1, '.', item, sep='')

def Update():
    index = int(input('position you want to update: '))
    if index <= len(stuff):
        stuff[index - 1] = input('Enter new stuff: ')
        Read()
    else:
        print('the position is not available')

def Delete():
    index = int(input('position you want to detele: '))
    if index <= len(stuff):
        del stuff[index - 1]
        Read()
    else:
        print('the position is not available')        

shopping = True
while shopping:
    letter = input('welcome to our shop, what do you want? (C R U D):')
    letter = letter.upper()
    if letter == 'C':
        Creat()
        print('to exit our store pls type "EXIT"')
    elif letter == 'R':
        Read()
        print('to exit our store pls type "EXIT"')
    elif letter == 'U':
        Update()
        print('to exit our store pls type "EXIT"')
    elif letter == 'D':
        Delete()
        print('to exit our store pls type "EXIT"')
    elif letter == 'EXIT':
        print('thanks for shopping with us! ')
        shopping = False
    else:
        print('wrong letter, pls try again')
