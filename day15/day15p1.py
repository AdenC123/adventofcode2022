# find ranges of scanned positions in each row,
# save unions of those ranges

# find taxicab distance from each sensor to beacon,
# scanned positions in current row will be 2d+1
# in each row above and below, scanned will be (2d+1)-2r
# where r is the abs distance from the center row

# subtract number of beacons in row at end

import re
from collections import namedtuple

filename = 'input.txt'
row = 2000000

Sensor = namedtuple('Sensor', 'x y bx by')
Range = namedtuple('Range', 'low high')

sensors = []
with open(filename) as f:
    for line in f:
        nums = re.findall(r'-?\d+', line)
        nums = [int(num) for num in nums]
        sensors.append(Sensor(nums[0], nums[1], nums[2], nums[3]))
        # sensors[nums[0], nums[1]] = nums[2], nums[3]

# keys: row, values: list of Range
ranges = {}
min_x = 0
max_x = 0


def update_min_max(r1, r2):
    global min_x, max_x
    min_x = min(r1.low, r2.low, min_x)
    max_x = max(r1.high, r2.high, max_x)


def union(r1, r2):
    # update_min_max(r1, r2)
    if r2.low <= r1.low and r2.high >= r1.high:
        # r1 inside r2
        return r2
    elif r1.low <= r2.low and r1.high >= r2.high:
        # r2 inside r1
        return r1
    elif r1.high >= r2.low >= r1.low:
        # r2 low inside r1
        return Range(r1.low, r2.high)
    elif r2.high >= r1.low >= r2.low:
        # r1 low inside r2
        return Range(r2.low, r1.high)
    else:
        # no overlap, keep separate
        return [r1, r2]


def union_list(lor):
    # try to combine all ranges with first range in lor
    # if one combines, replace first range with new range and repeat
    # if none combine, move first of lor to result and repeat
    lor = lor.copy()
    if len(lor) == 0:
        return []
    else:
        first = lor[0]
        rest = lor[1:]
        for i in range(len(rest)):
            u = union(first, rest[i])
            if type(u) != list:
                rest.pop(i)
                return union_list([u] + rest)
        return [first] + union_list(rest)


# assert union_list([Range(0, 10)]) == [Range(0, 10)]
# assert union_list([Range(0, 10), Range(9, 13)]) == [Range(0, 13)]
# assert union_list([Range(0, 10), Range(9, 13),
#                    Range(12, 18)]) == [Range(0, 18)]
# assert union_list([Range(0, 10), Range(12, 18),
#                    Range(9, 13)]) == [Range(0, 18)]
# assert union_list([Range(0, 1), Range(3, 4),
#                    Range(6, 7)]) == [Range(0, 1),
#                                      Range(3, 4),
#                                      Range(6, 7)]


def add_ranges(sensor):
    # add all row ranges from sensor to beacon
    dist = abs(sensor.x - sensor.bx) + abs(sensor.y - sensor.by)
    for i in range(dist + 1):
        new_range = Range(sensor.x - dist + i,
                          sensor.x + dist - i)
        # ranges above and below (same for first)
        up_y = sensor.y + i
        down_y = sensor.y - i
        if up_y in ranges.keys():
            ranges[up_y] = union_list([new_range] + ranges[up_y])
        else:
            ranges[up_y] = [new_range]

        if down_y in ranges.keys():
            ranges[down_y] = union_list([new_range] + ranges[down_y])
        else:
            ranges[down_y] = [new_range]


def total_range(lor):
    sum = 0
    for r in lor:
        sum += abs(r.low - r.high) + 1
    return sum


def row_beacons(y):
    result = set()
    for s in sensors:
        if s.by == y:
            result.add((s.bx, s.by))
    return result


def row_sensors(y):
    result = set()
    for s in sensors:
        if s.y == y:
            result.add((s.x, s.y))
    return result


def print_all():
    for y in ranges.keys():
        bs = row_beacons(y)
        ss = row_sensors(y)
        rs = ranges[y]
        all_vals = []
        for r in rs:
            for i in range(r.low, r.high + 1):
                all_vals.append(i)
        for x in range(min_x, max_x + 1):
            if (x, y) in ss:
                print('S', end='')
            elif (x, y) in bs:
                print('B', end='')
            elif x in all_vals:
                print('#', end='')
            else:
                print('.', end='')
        print(y)
    print()


for sensor in sensors:
    add_ranges(sensor)
    print('sensor done')
    # ranges = dict(sorted(ranges.items()))
    # print_all()

# ranges = dict(sorted(ranges.items()))
# print_all()

total = total_range(ranges[row])
total -= len(row_beacons(row))
print(f'Total: {total}')
