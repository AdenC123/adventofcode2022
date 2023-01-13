from collections import namedtuple

filename = 'input.txt'
Cube = namedtuple('Cube', 'x y z')
cubes = []

max_coord = 0
total_cubes = 0

with open(filename) as f:
    for line in f:
        nums = line.strip().split(',')
        cubes.append(Cube(int(nums[0]), int(nums[1]), int(nums[2])))
        max_coord = max(int(nums[0]), int(nums[1]), int(nums[2]), max_coord)
        total_cubes += 1


def all_sides(c):
    return (Cube(c.x + 1, c.y, c.z),
            Cube(c.x - 1, c.y, c.z),
            Cube(c.x, c.y + 1, c.z),
            Cube(c.x, c.y - 1, c.z),
            Cube(c.x, c.y, c.z + 1),
            Cube(c.x, c.y, c.z - 1))


def outside(start_side):
    queue = [start_side]
    visited = []
    while queue:
        side = queue.pop()
        # base cases: already visited, is a cube, or is outside the max
        if side in visited:
            continue
        elif side in cubes:
            continue
        elif side.x > max_coord or side.y > max_coord or side.z > max_coord:
            return True

        visited.append(side)
        queue = list(all_sides(side)) + queue

    return False


def solve():
    result = 0
    checked = 0
    for cube in cubes:
        for side in all_sides(cube):
            if outside(side):
                result += 1
        checked += 1
        print(f'\rChecked {checked} out of {total_cubes} cubes', end='')
    return result


print(f'\nSurface area: {solve()}')
