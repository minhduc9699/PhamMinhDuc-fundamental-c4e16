fontC = int(input('chose font size for the letter C:'))
fontO = int(input('chose font size for the letter O:'))
fontD = int(input('chose font size for the letter D:'))
fontE = int(input('chose font size for the letter E:'))


### Letter C:
output_strC = ''
for rowC in range (0, fontC):
    for columnC in range (0, fontC):
        if columnC == 1 or (rowC == 0 or rowC == fontC - 1) and (columnC > 1 and columnC < fontC + 1):
            output_strC += '*'
        else:
            output_strC += ' '
    output_strC += '\n'
print(output_strC, end='')


### Letter O:
output_strO = ''
for rowO in range(0, fontO):
    for columnO in range(0, fontO):
        if (columnO == 1 or columnO == fontO - 2 ) and rowO != 0 and rowO != fontO - 1  or ((rowO == 0 or rowO == fontO - 1) and columnO > 1 and columnO < fontO - 2):
            output_strO += '*'
        else:
            output_strO += ' '
    output_strO += '\n'
print(output_strO, end='')



### letter D:
output_strD = ''
if fontD < 5:
    print('font size must bigger than 4')
else:
    for rowD in range(0, fontD):
        for columnD in range(0, fontD):
            if columnD == 1 or (rowD == 0 or rowD == fontD - 1) and (columnD > 1 and columnD < fontD - 2) or (columnD == fontD -2 and rowD != 0 and rowD != fontD -1):
                output_strD += '*'
            else:
                output_strD += ' '
        output_strD += "\n"
    print(output_strD, end='')




#letter E:
output_strE=""
if fontE % 2 == 0:
    print('font size E must be an odd number')
else:
    for rowE in range (0, fontE):
        for columnE in range(0, fontE):
            if columnE == 1 or ((rowE == 0 or rowE == fontE - 1) and (columnE > 1 and columnE < fontE - 1)) or (rowE == (fontE - 1) / 2 and columnE > 1 and columnE < fontE - 1):
                output_strE += '*'
            else:
                output_strE += ' '
        output_strE += '\n'
        print(output_strE, end='')
