sizes = {1: 0}
cur_dirs = [1]

with open('input.txt') as f:
    f.readline()
    for line in f:
        line = line.strip()
        dirSize = 0
        if line.startswith('$ cd ..'):
            cur_dirs.pop()
        elif line.startswith('$ cd'):
            dir_id = list(sizes.keys())[-1] + 1
            if dir_id in sizes.keys():
                print('Duplicate ' + dir_id)
            sizes[dir_id] = 0
            cur_dirs.append(dir_id)
        elif line.startswith('$ ls'):
            pass
        elif line.startswith('dir'):
            pass
        else:
            size = int(line.split()[0])
            for dir in cur_dirs:
                sizes[dir] += size

print(sizes)
unused = 70000000 - sizes[1]
rsf = float('inf')
for size in sizes.values():
    if unused + size >= 30000000 and size < rsf:
        rsf = size

print(rsf)
