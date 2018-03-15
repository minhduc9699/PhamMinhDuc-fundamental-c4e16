teencode  = {
    'hc' : 'học',
    'ng' : 'người',
    'pt' : 'phát triển',
    'ns' : 'nói',
    'lm' : 'làm',
    'stt' : 'số thứ tự',
}
while True:
    print('*' * 20)
    for key in teencode:
        print(key, end='\t')
    print('\n')

    yourcode = input('yourcode? ')
    if yourcode in teencode:
        print('trans: ', teencode[yourcode])
    else:
        Y_N_input = input('not found, do you want to contribute this word? (Y/N)? ').upper()
        if Y_N_input == 'Y':
            teencode[yourcode] = input('enter your trans: ')
            print('updated')
        else:
            break
