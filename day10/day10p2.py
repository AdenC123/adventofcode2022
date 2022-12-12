prog = []
check = (20, 60, 100, 140, 180, 220)

with open('input.txt') as f:
    for line in f:
        prog.append(line.strip())

cycle = 0
x = 1
wait = 0
hold_val = 0

img = []


def add_img(cycle, x):
    sprite = (x, x+1, x+2)
    if cycle % 40 in sprite:
        img.append('#')
    else:
        img.append('.')


while prog or hold_val:
    cycle += 1
    # print(f'During cycle {cycle} x is {x}')

    add_img(cycle, x)

    if hold_val:
        x += hold_val
        hold_val = 0
    else:
        ins = prog.pop(0)
        if ins == 'noop':
            pass
        else:
            hold_val = int(ins.split()[1])
            wait = 1

    # print(f'After cycle {cycle} x is {x}')
print(len(img))
cur_line = ''
for i in range(1, len(img)):
    cur_line = cur_line + img[i-1]
    if i % 40 == 0:
        print(cur_line)
        cur_line = ''
print(cur_line)
