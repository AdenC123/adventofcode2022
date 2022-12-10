data = []

with open('input.txt') as f:
    for line in f:
        data.append(line.strip())


def all_elves():
    res = []
    current_elf = 0
    for x in data:
        if x == '':
            res.append(current_elf)
            current_elf = 0
        else:
            current_elf += int(x)
    return res


elves = all_elves()
elves.sort(reverse=True)
print(elves[0])

# maxElf = 0
# for n in data:
#     if n == '':
#         if currentElf > maxElf:
#             maxElf = currentElf
#         currentElf = 0
#     else:
#         currentElf += int(n)
#
# print(maxElf)
