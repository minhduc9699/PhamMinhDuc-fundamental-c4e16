prices = {
    'banana' : 4,
    'apple' : 2,
    'orange' : 1.5,
    'pear' : 3,
}

stock = {
    'banana' : 6,
    'apple' : 0,
    'orange' : 32,
    'pear' : 15,
}

for key in prices and stock:
    print(key)
    print('prices: ', prices.get(key))
    print('stock: ', stock.get(key))
    print('*' * 20)

total = 0
for key in prices:
    key_sell = prices[key] * stock[key]
    total += key_sell
    print('money you can get from', key, ': $', key_sell)
print('total money you can get: $', total)
