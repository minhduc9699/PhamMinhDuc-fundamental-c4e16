str_input = input().lower()


count_x = str_input.count('x')
count_o = str_input.count('o')

if count_x == count_o:
    print(True)
else:
    print(False)
