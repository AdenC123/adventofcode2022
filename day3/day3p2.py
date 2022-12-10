import string

data = []
alphabet = string.ascii_lowercase + string.ascii_uppercase

with open('input.txt') as f:
    for line in f:
        data.append(line.strip())


sum = 0
while len(data) > 0:
    sack1 = set(data.pop())
    sack2 = set(data.pop())
    sack3 = set(data.pop())
    unique = list(sack1.intersection(sack2).intersection(sack3))[0]
    print(unique)
    sum += alphabet.index(unique) + 1

print(sum)
