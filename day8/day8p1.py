import numpy as np

matrix = []

with open('input.txt') as f:
    for line in f:
        row = []
        for c in line.strip():
            row.append(int(c))
        matrix.append(row)

matrix = np.array(matrix)
print(matrix)


def check_lists(val, left, right):
    # edge check
    if len(left) == 0 or len(right) == 0:
        return True

    # visibility check
    visible_left = True
    visible_right = True
    for num in left:
        if num >= val:
            visible_left = False
            break
    for num in right:
        if num >= val:
            visible_right = False
            break
    return visible_left or visible_right


def check_row(x, y):
    val = matrix[y, x]
    row = matrix[y]
    left = row[:x]
    right = row[x+1:]
    return check_lists(val, left, right)


def check_column(x, y):
    val = matrix[y, x]
    col = matrix[:, x]
    up = col[:y]
    down = col[y+1:]
    return check_lists(val, up, down)


count = 0
for y in range(matrix.shape[0]):
    for x in range(matrix.shape[1]):
        if check_row(x, y) or check_column(x, y):
            count += 1

print(count)


