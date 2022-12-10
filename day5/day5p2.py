import re

data = [[] for _ in range(9)]
prog = []

with open('input.txt') as f:
    # parse initial stacks into data
    for _ in range(8):
        line = f.readline()
        newline = ''
        for c in line.strip():
            if c not in '[] ':
                newline = newline + c
        # print(newline)

        for i in range(len(newline)):
             c = newline[i]
             if c != 'x':
                 data[i].append(c)

    # skip 2 lines
    f.readline()
    f.readline()

    # parse program
    for line in f:
        prog.append(re.sub(r'\D', '', line))


def move(num, start, end):
    if len(data[start]) > num-1:
        temp = []
        for _ in range(num):
            temp.append(data[start].pop(0))
        data[end] = temp + data[end]


for p in prog:
    if len(p) == 3:
        num = int(p[0])
        start = int(p[1]) - 1
        end = int(p[2]) - 1
    else:
        num = int(p[0:2])
        start = int(p[2]) - 1
        end = int(p[3]) - 1
    move(num, start, end)

print(data)
result = ''
for l in data:
    if len(l) > 0:
        result = result + l[0]

print(result)
