import re
from collections import namedtuple

# STRUCTURES
Point = namedtuple('Point', 'x y')

# GLOBALS
UP = Point(0, -1)
DOWN = Point(0, 1)
LEFT = Point(-1, 0)
RIGHT = Point(1, 0)

FACING_PASS = {
    RIGHT: 0,
    DOWN: 1,
    LEFT: 2,
    UP: 3
}

FACING_PRINT = {
    RIGHT: '>',
    DOWN: 'v',
    LEFT: '<',
    UP: '^'
}

NEXT_FACING_RIGHT = {
    UP: RIGHT,
    RIGHT: DOWN,
    DOWN: LEFT,
    LEFT: UP
}
NEXT_FACING_LEFT = {f2: f1 for f1, f2 in NEXT_FACING_RIGHT.items()}


# MAIN
def move_ignore_val(pos, facing, graph) -> Point:
    next_pos = Point(*map(sum, zip(pos, facing)))
    return Point(next_pos.x % len(graph[0]), next_pos.y % len(graph))


def get_next_pos(pos, steps, facing, graph) -> Point:
    for _ in range(steps):
        next_pos = move_ignore_val(pos, facing, graph)
        next_val = graph[next_pos.y][next_pos.x]
        if next_val == ' ':
            # keep going until other side of graph
            while next_val == ' ':
                next_pos = move_ignore_val(next_pos, facing, graph)
                next_val = graph[next_pos.y][next_pos.x]
        if next_val == '#':
            # stop early
            return pos
        else:
            graph[pos.y] = graph[pos.y][:pos.x] + FACING_PRINT[facing] + graph[pos.y][pos.x+1:]
        pos = next_pos
    return pos


def part1(lines) -> int:
    # store graph in matrix
    max_len = max(map(len, lines[:-1])) - 1
    graph = [line[:-1] for line in lines[:-2]]
    for i in range(len(graph)):
        graph[i] += ' ' * (max_len - len(graph[i]))
    # do instructions
    pos = Point(graph[0].index('.'), 0)
    graph[pos.y] = graph[pos.y][:pos.x] + '>' + graph[pos.y][pos.x+1:]
    facing = RIGHT
    path = lines[-1]
    while path:
        if path[0].isdigit():
            steps = int(re.search(r'\d+', path).group())
            path = path.lstrip('0123456789')
            pos = get_next_pos(pos, steps, facing, graph)
        elif path[0] == 'R':
            facing = NEXT_FACING_RIGHT[facing]
            path = path[1:]
        elif path[0] == 'L':
            facing = NEXT_FACING_LEFT[facing]
            path = path[1:]
    graph[pos.y] = graph[pos.y][:pos.x] + '*' + graph[pos.y][pos.x+1:]
    for row in graph:
        print(row)
    return ((pos.y+1) * 1000) + ((pos.x+1) * 4) + FACING_PASS[facing]


def part2(lines) -> int:
    return 0


def main():
    with open("test.txt") as f:
        lines = f.readlines()
        print("Part 1 Test: " + str(part1(lines)))
        # print("Part 2 Test: " + str(part2(lines)))
    with open("input.txt") as f:
        lines = f.readlines()
        print("Part 1 Input: " + str(part1(lines)))
        # print("Part 2 Input: " + str(part2(lines)))


if __name__ == '__main__':
    main()
