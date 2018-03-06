
#method 1:

'''
from math import factorial
num = int(input('enter a number: '))
num = factorial(num)
print(num)
'''

#menthod 2:

num = int(input('enter a number: '))
fac = 1
for i in range(1, num + 1):
    fac *= i
print(fac)
