num_bacteria = int(input('how many bacterias are there? '))
time_bacteria = int(input('how much time in minutes will we wait? '))

total = int(num_bacteria * 2 ** (time_bacteria / 2))

print('after %d minutes, we would have %d bacterias' % (time_bacteria, total))
