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
print(elves[0] + elves[1] + elves[2])


# currentElf = 0
# maxElf1 = 0
# maxElf2 = 0
# maxElf3 = 0
# for n in data:
#
#     if n == '':
#         if currentElf > maxElf1:
#             maxElf3 = maxElf2
#             maxElf2 = maxElf1
#             maxElf1 = currentElf
#         elif currentElf > maxElf2:
#             maxElf3 = maxElf2
#             maxElf2 = currentElf
#         elif currentElf > maxElf3:
#             maxElf3 = currentElf
#         currentElf = 0
#
#     else:
#         currentElf += int(n)
#
# print(maxElf1 + maxElf2 + maxElf3)