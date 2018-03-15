numbers = [1, 4, 5, 1, 5, 8, 4, 9, 2, 0, 1]
print(numbers)
num_to_count = int(input('enter a number: '))
count = 0

for i in numbers:
    if i == num_to_count:
        count += 1
print(num_to_count, 'appears', count, 'times in my list')
