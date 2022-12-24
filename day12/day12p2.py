from dataclasses import dataclass


@dataclass
class Pos:
    x: int
    y: int


file_name = 'input.txt'
start_pos = Pos(149, 20)

# file_name = 'test.txt'
# start_pos = Pos(5, 2)

maze = []
with open(file_name) as f:
    for line in f:
        maze.append(line.strip())

max_x = len(maze[0]) - 1
max_y = len(maze) - 1


def get_val(pos):
    return maze[pos.y][pos.x]


assert get_val(start_pos) == 'E'


def valid(path):
    to_pos = path[-2]
    from_pos = path[-1]

    if from_pos.x > max_x or from_pos.y > max_y:
        return False
    if from_pos.x < 0 or from_pos.y < 0:
        return False

    # print(f'to: {to_pos} from: {from_pos}')
    to_val = get_val(to_pos)
    from_val = get_val(from_pos)
    if from_val == 'S':
        from_val = 'a'
    if to_val == 'E':
        to_val = 'z'

    if ord(to_val) - ord(from_val) > 1:
        return False

    return True


def next_positions(p):
    return (Pos(p.x + 1, p.y),
            Pos(p.x,     p.y + 1),
            Pos(p.x - 1, p.y),
            Pos(p.x,     p.y - 1))


def all_next_paths(path):
    pos = path[-1]
    result = []
    for next_pos in next_positions(pos):
        result.append(path + [next_pos])
    return result


def next_valid_paths(path):
    next_paths = all_next_paths(path)
    result = []
    for new_path in next_paths:
        if valid(new_path):
            result.append(new_path)
    return result


def bfs(start):
    visited = []
    queue = [[start]]

    while queue:
        path = queue.pop(0)
        pos = path[-1]
        # print(f'Current path: {path}')

        # end of maze check
        if get_val(pos) == 'a':
            return path

        # visited check
        if pos in visited:
            continue

        visited.append(pos)
        next_paths = next_valid_paths(path)
        queue = queue + next_paths

    # failed
    return


shortest_path = bfs(start_pos)
if shortest_path:
    print('Shortest path found!')
    print(shortest_path)
    print(f'Steps: {len(shortest_path) - 1}')
else:
    print('No path found')
