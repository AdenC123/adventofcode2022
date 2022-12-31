filename = 'test.txt'
total_to_drop = 2022

with open(filename) as f:
    jets = list(f.readline().strip())

rows = ['#######']

shapes = [['..####.'],

          ['...#...',
           '..###..',
           '...#...'],

          ['..###..',
           '....#..',
           '....#..'],

          ['..#....',
           '..#....',
           '..#....',
           '..#....'],

          ['..##...',
           '..##...']]


def print_rows():
    rs = rows.copy()
    rs.pop(0)
    rs.reverse()
    for row in rs:
        print(f'|{row}|')
    print('+-------+\n')


def overlap(new, old):
    for i in range(len(new)):
        if new[i] == '#' and old[i] == '#':
            return True
    return False


def move(shape, height):
    # return new shape string after jet move (may be same)
    jet = jets.pop(0)
    jets.append(jet)

    new_shape = []
    for row in shape:
        if jet == '<':
            # try to move row left, or end at wall
            if row[0] == '#':
                return shape
            else:
                row = row[1:] + row[0]
                new_shape.append(row)
        else:
            # try to move row right, or end at wall
            if row[-1] == '#':
                return shape
            else:
                row = row[-1] + row[:-1]
                new_shape.append(row)
        # if we are in rows, check if moved row and current row overlap
        if height < 0 and overlap(row, rows[height]):
            return shape

        height += 1

    return new_shape


def union(row1, row2):
    result = ''
    for i in range(len(row1)):
        if row1[i] == '#' or row2[i] == '#':
            result += '#'
        else:
            result += '.'
    return result


def add_to_rows(shape, height):
    for row in shape:
        if height < 0:
            rows[height] = union(row, rows[height])
        else:
            rows.append(row)
        height += 1


def drop_shape():
    shape = shapes.pop(0)
    shapes.append(shape)
    # height -1 is where rows starts
    height = 3

    while True:
        # try to move shape by jet
        shape = move(shape, height)

        # if it can be dropped, drop it, otherwise add it to rows and stop
        if height > 0 or not overlap(shape[0], rows[height-1]):
            height -= 1
        else:
            add_to_rows(shape, height)
            break


for _ in range(20):
    drop_shape()
    print(f'Height: {len(rows) - 1}')
    print_rows()

final = len(rows) - 1
print(f'Final height: {final}')
