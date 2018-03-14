def distance (x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    ds = dx * dx + dy * dy
    result = ds ** 0.5
    print(result)
x1 = int(input('enter a number'))
x2 = int(input('enter a number'))
x3 = int(input('enter a number'))
x4 = int(input('enter a number'))
distance(x1, x2, x3, x4)
