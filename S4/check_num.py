n = int(input('enter a nber: '))

is_prime = True

'''
faster way
for i in range(2,n - 1):
    if n % i == 0:
        is_prime = False
        break
'''
i = 2

while i <= (n ** 0.5):
    if n % i:
        is_prime = False
        break
    i += 1
if is_prime == True:
    print(n, 'is a prime nber')
else:
    print(n, 'is not a prime nber')
