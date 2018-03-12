name = input('enter your name: ')
name = name.lower()
name = name.title()
name = name.strip()
for i in range(len(name)):
    name = name.replace('  ', ' ')
print('updated:', name)
