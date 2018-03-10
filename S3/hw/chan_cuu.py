sheep_size = [4, 47, 34, 346, 32, 25, 90]

def shear():
    sheep_size_biggest = max(sheep_size)
    print('now my biggest sheep size is %d, lets shear it' % sheep_size_biggest)
    for index, item in enumerate(sheep_size):
        if item == sheep_size_biggest:
            sheep_size[index] = 8
    print('after shearing here my flock: ')
    print(sheep_size, sep=' ')

def grow(i):
    global sheep_size
    sheep_size = [x + i for x in sheep_size]
    print('One month has passed, now here my flock')
    print(sheep_size)

def sell():
    total_size = sum(sheep_size)
    sell_money = total_size * 2
    print('My flock have size in total %d' % total_size)
    print('i would get', total_size, '* 2$ = ', sell_money,'$')


print('*' * 20)
print('hello, my name is Duc, and here is my flock: ')
print(sheep_size)
print('\n')
shear()
print('\n')
for i in range(4):
    grow(50)
    shear()
    print('\n')
sell()
