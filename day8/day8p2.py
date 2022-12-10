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


def count_trees(val, lst):
    count = 0
    for tree in lst:
        if val <= tree:
            return count + 1
        else:
            count += 1
    return count


def score_coords(x, y):
    val = matrix[y, x]
    col = matrix[:, x]
    row = matrix[y]
    left = np.flip(row[:x])
    right = row[x + 1:]
    down = col[y + 1:]
    up = np.flip(col[:y])
    score = count_trees(val, left) * count_trees(val, right) * \
        count_trees(val, up) * count_trees(val, down)
    return score


max_score = 0
for y in range(matrix.shape[0]):
    for x in range(matrix.shape[1]):
        score = score_coords(x, y)
        if score > max_score:
            max_score = score

print(max_score)

