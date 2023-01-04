filename = 'input.txt'
total_to_drop = 1000000000000

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


def can_drop(shape, height):
    for row in shape:
        if height > 0:
            return True
        if overlap(row, rows[height-1]):
            return False
        height += 1
    return True


def drop_shape():
    shape = shapes.pop(0)
    shapes.append(shape)
    # height -1 is where rows starts
    height = 3

    while True:
        # try to move shape by jet
        shape = move(shape, height)

        # if it can be dropped, drop it, otherwise add it to rows and stop
        if can_drop(shape, height):
            height -= 1
        else:
            add_to_rows(shape, height)
            break


def detect_cycle(nums):
    # find a repeat of len 30? or greater in nums
    length = 30
    max_length = len(nums) / 2
    while length < max_length:
        if nums[-length:] == nums[-length*2:-length]:
            return length
        else:
            length += 1
    return False


def find_height(num_to_drop):
    dropped = 0
    last_height = 0
    skip_height = 0
    delta_heights = []
    while dropped < num_to_drop:
        # look for cycles if we haven't skipped already
        if not skip_height:
            cycle_length = detect_cycle(delta_heights)
            if cycle_length:
                # cycle found!
                cycle_height = sum(delta_heights[-cycle_length:])
                print(f'\nCycle detected at rock {dropped}'
                      f' with length {cycle_length}'
                      f' and height {cycle_height}')

                num_cycles = (num_to_drop - dropped) // cycle_length
                skip_height = num_cycles * cycle_height
                dropped += num_cycles * cycle_length

            elif dropped % 100 == 0:
                print(f'\rNo cycles detected by rock {dropped}', end='')

        # drop 1 shape and update delta heights
        drop_shape()
        dropped += 1
        cur_height = len(rows) - 1
        delta_heights.append(cur_height - last_height)
        last_height = cur_height

    return len(rows)-1 + skip_height


final = find_height(total_to_drop)
print(f'Final height: {final}')

# for i in range(total_to_drop):
#     drop_shape()
#     if i % 10000 == 0:
#         print(f'\rRock {i} processed', end='')
#     # print_rows()
#
# final = len(rows) - 1
# print(f'Final height: {final}')
