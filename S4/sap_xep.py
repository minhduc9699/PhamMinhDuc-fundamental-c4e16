num = [-23, 235, -24, 3245, 36, 35, -346]

sorted_list = []

while True:
    sorted_list.append(min(num))
    num.remove(min(num))
    if len(num) == 0:
        break
print(sorted_list)
