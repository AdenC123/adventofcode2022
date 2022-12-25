filename = 'input.txt'
# cave = [Pos(500, 0, '+')]
cave = {(500, 0): '+'}

max_y = 0
min_x = 500
max_x = 500


def print_cave():
    for y in range(0, max_y+1):
        for x in range(min_x, max_x+1):
            if (x, y) in cave:
                print(cave[x, y], end='')
            else:
                print('.', end='')
        print(f' {y}')
    print()


def create_line(last_x, x, last_y, y):
    if last_x < x:
        for i in range(last_x, x+1):
            cave[(i, y)] = '#'
    elif last_x > x:
        for i in range(x, last_x+1):
            cave[(i, y)] = '#'
    elif last_y < y:
        for i in range(last_y, y+1):
            cave[(x, i)] = '#'
    else:
        for i in range(y, last_y+1):
            cave[(x, i)] = '#'


def create_wall(line):
    # print(f'Wall: {line}')
    points = line.split(' -> ')
    first_point = points.pop(0)
    last_x = int(first_point.split(',')[0])
    last_y = int(first_point.split(',')[1])
    for point in points:
        # create line
        x, y = point.split(',')
        x = int(x)
        y = int(y)
        create_line(last_x, x, last_y, y)

        # update maxes
        global max_y, max_x, min_x
        max_y = max(max_y, last_y, y)
        max_x = max(max_x, last_x, x)
        min_x = min(min_x, last_x, x)

        # update last position
        last_x = x
        last_y = y


with open(filename) as f:
    for line in f:
        create_wall(line.strip())


# print_cave()
# print(f'Min x: {min_x}\nMax x: {max_x}\nMax y: {max_y}')


def next_pos(pos):
    # None if no more moves (at rest), pos if next
    x, y = pos
    if (x, y+1) not in cave.keys():
        return x, y+1
    elif (x-1, y+1) not in cave.keys():
        return x-1, y+1
    elif (x+1, y+1) not in cave.keys():
        return x+1, y+1
    else:
        return False


def add_sand():
    # False if drop below max, pos if rest
    pos = 500, 0
    next = next_pos(pos)
    while next:
        # check if off edge
        x, y = next
        if y >= max_y:
            return False
        pos = next
        next = next_pos(pos)
    return pos


# simulate sand
count = 0
while True:
    result = add_sand()
    if result:
        x, y = result
        cave[(x, y)] = 'o'
        count += 1
    else:
        break

print_cave()
print(f'Sand count: {count}')