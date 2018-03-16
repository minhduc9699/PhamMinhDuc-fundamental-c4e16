def print_inventory():
    print('*' * 30)
    for key, value in inventory.items():
        print(key, value)

inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
#add a key
inventory['pocket'] = []
print_inventory()

#set value
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
print_inventory()

#remove
inventory['backpack'].remove('dagger')
print_inventory()

#add a num
inventory['gold'] += 50
print_inventory()
