def sorting():
    sorted_list = []
    while True:
        sorted_list.append(min(numbers))
        numbers.remove(min(numbers))
        if len(numbers) == 0:
            break
    print('sorted list')
    print(sorted_list)

num = input('enter a sequence of number, separated by space: ')

#strip: cut spaces at start/end of string
list_num = num.strip().split()

numbers = []

for item in list_num:
    numbers.append(int(item))
print(numbers)

is_sorted = True
for i in range(len(numbers) - 1):
    if numbers[i] > numbers[i + 1]:
        is_sorted = False
        break
if is_sorted:
    print('your list is already sorted')
else:
    print('your list is not sorted')
    sorting()
