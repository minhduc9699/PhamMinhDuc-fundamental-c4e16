numbers = [1, 4, 5, 1, 5, 8, 4, 9, 2, 0, 1]
print(numbers)

num = int(input('enter numner you want to count: '))

num_count = numbers.count(num)

print('%d appears %d times in my list' % (num, num_count))
