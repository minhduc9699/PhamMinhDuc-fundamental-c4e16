fthing = ['C', 'C++', 'C#', 'Java']

print('Hi there, here your favorite things so far')
print(*fthing, sep=', ')
fthing.append(input('name thing you want to add '))
print(*fthing, sep=', ')
