import string

sacks = []
alphabet = string.ascii_lowercase + string.ascii_uppercase

with open('input.txt') as f:
    for line in f:
        sacks.append(line.strip())


def split(s):
    half = int(len(s) / 2)
    firstHalf = s[:half]
    secondHalf = s[half:]
    # print(len(firstHalf), len(secondHalf))
    return [firstHalf, secondHalf]


sacks = list(map(split, sacks))

sum = 0
for sack in sacks:
    unique = list(set(sack[0]).intersection(set(sack[1])))[0]
    sum += alphabet.index(unique) + 1

print(sum)
