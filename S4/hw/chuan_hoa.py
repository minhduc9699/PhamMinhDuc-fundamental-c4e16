def chuan_hoa_ten():
    name = input('enter your name: ')
    name = name.lower()
    name = name.title()
    name = name.strip()
    for i in range(len(name)):
        name = name.replace('  ', ' ')
    print('updated:', name)

def chuan_hoa_so():
    num = int(input('enter your balance: '))

    updated_num = '{:,}'.format(num)

    print('your updated balance: ${0} '.format(updated_num))

chuan_hoa_ten()
chuan_hoa_so()
