pair_of_rabbit = [1]
month_input = int(input('enter number of month you want: '))
for i in range(1, month_input + 1):
    pair_of_rabbit.append(pair_of_rabbit[i - 1] + pair_of_rabbit[i - 2])
for month, total in enumerate(pair_of_rabbit):
    print('Month', month, ':' , total, 'pair of rabbit')
