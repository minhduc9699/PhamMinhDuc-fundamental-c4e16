fthing = ['C', 'C++', 'C#', 'Java']
print('*' * 20)
for index, item in enumerate(fthing):
    print(index + 1, '.', item, sep='')
print('*' * 20)

index = int(input('position you want to upadte: '))
fthing[index - 1] = str(input('name your update: '))

for index, item in enumerate(fthing):
    print(index + 1, '. ', item, sep='')
