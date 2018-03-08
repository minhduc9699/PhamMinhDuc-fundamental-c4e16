fthing = ['C', 'C++', 'C#', 'Java']
print('*' * 20)
for index, item in enumerate(fthing):
    print(index + 1, '.', item, sep='')
print('*' * 20)

index = input('name you want to get rid of: ')

if index in fthing:
    fthing.remove(index)
else:
    print('Not found')
#fthing.pop[index - 1]
#del fthing[index - 1]
for index, item in enumerate(fthing):
    print(index + 1, '. ', item, sep='')
