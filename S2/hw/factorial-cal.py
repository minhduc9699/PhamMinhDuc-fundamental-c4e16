
'''
from math import factorial
num = int(input('enter a number: '))
num = factorial(num)
print(num)
'''
num = int(input('enter a number: '))
fac = 1
for i in range(1, num + 1):
    fac *= i
print(fac)
