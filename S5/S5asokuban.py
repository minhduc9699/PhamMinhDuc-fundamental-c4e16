map_sokoban = {
    "x" : 5,
    "y" : 5,
}

player = {
    'x' : 0,
    'y' : 4,
}

boxes = [
    {'x' : 1, 'y' : 1},
    {'x' : 2, 'y' : 2},
    {'x' : 3, 'y' : 3},
]

des = [
    {'x' : 2, 'y' : 1},
    {'x' : 3, 'y' : 2},
    {'x' : 4, 'y' : 3},
]
while True:

    for y in range(map_sokoban['y']):
        for x in range(map_sokoban['x']):

            player_is_here = False
            des_is_here = False
            box_is_here = False
            for de in des:
                if de['x'] == x and de['y'] == y:
                    des_is_here = True
                    break
            for box in boxes:
                if box['x'] == x and box['y'] == y:
                    box_is_here = True
                    break
            if x == player['x'] and y == player['y']:
                player_is_here = True

            if box_is_here:
                print('B', end=' ')
            elif des_is_here:
                print('D', end=' ')
            elif player_is_here:
                print('P', end=' ')
            else:
                print('-', end=' ')
        print()
    ###### end of print map
    is_win = True
    for box in boxes:
        if box not in des:
            is_win = False

    if is_win:
        print('you win')
        break


    move = input('Your move? ').upper()

    dx = 0
    dy = 0

    if move == 'W':
        print('Up')
        dy = -1
    elif move == 'S':
        print('Down')
        dy = 1
    elif move == 'A':
        print('Left')
        dx = -1
    elif move == 'D':
        print('Right')
        dx = 1

    if 0 <= player['x'] + dx < map_sokoban['x'] \
    and 0 <= player['y'] + dy < map_sokoban['y']:
        player['x'] += dx
        player['y'] += dy

    for box in boxes:
        if 0 <= box['x'] + dx < map_sokoban['x'] \
        and 0 <= box['y'] + dy < map_sokoban['y']:
            if player['x'] == box['x'] and player['y'] == box['y']:
                box['x'] += dx
                box['y'] += dy
