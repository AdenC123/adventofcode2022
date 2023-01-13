from collections import namedtuple

filename = 'input.txt'
Cube = namedtuple('Cube', 'x y z')
cubes = []

with open(filename) as f:
    for line in f:
        nums = line.strip().split(',')
        cubes.append(Cube(int(nums[0]), int(nums[1]), int(nums[2])))


def all_sides(c):
    return (Cube(c.x + 1, c.y, c.z),
            Cube(c.x - 1, c.y, c.z),
            Cube(c.x, c.y + 1, c.z),
            Cube(c.x, c.y - 1, c.z),
            Cube(c.x, c.y, c.z + 1),
            Cube(c.x, c.y, c.z - 1))


def solve():
    result = 0
    for cube in cubes:
        for side in all_sides(cube):
            if side not in cubes:
                result += 1
    return result


print(f'Surface area: {solve()}')
