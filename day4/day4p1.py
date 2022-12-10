data = []

with open('input.txt') as f:
    for line in f:
        data.append(line.strip().split(','))

count = 0
for pair in data:
    n1 = int(pair[0].split('-')[0])
    n2 = int(pair[0].split('-')[1])
    n3 = int(pair[1].split('-')[0])
    n4 = int(pair[1].split('-')[1])

    if n3 <= n1 and n4 >= n2:
        count += 1
    elif n1 <= n3 and n2 >= n4:
        count += 1

print(count)