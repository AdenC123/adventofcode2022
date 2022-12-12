from dataclasses import dataclass

file_name = 'input.txt'


@dataclass
class Monkey:
    items: list
    op: str
    test: int
    true: int
    false: int
    inspects: int


monkeys = {}


# process monkeys into dict
def to_items(s):
    items = []
    for item in s.split():
        items.append(int(item.replace(',', '')))
    return items


def make_monkey(m):
    lines = m.split('\n')
    id = int(lines[0][7])
    items = to_items(lines[1][18:])
    op = lines[2][19:]
    test = int(lines[3][21:])
    true = int(lines[4][-1])
    false = int(lines[5][-1])

    monkeys[id] = Monkey(items, op, test, true, false, 0)


with open(file_name) as f:
    m = ''
    for line in f:
        if line == '\n':
            make_monkey(m)
            m = ''
        else:
            m += line
    make_monkey(m)


# do program
def do_op(item, op):
    old = item
    return eval(op)


max_mod = 1
for monkey in monkeys.values():
    max_mod *= monkey.test
print(f'max_mod: {max_mod}')

def take_turn(monkey):
    while monkey.items:
        item = monkey.items.pop(0)
        monkey.inspects += 1
        new_item = do_op(item, monkey.op)
        # removed for part 2
        # new_item = new_item // 3
        if new_item % monkey.test == 0:
            throw_id = monkey.true
        else:
            throw_id = monkey.false
        # prevent large numbers
        new_item = new_item % max_mod
        monkeys[throw_id].items.append(new_item)


for i in range(10000):
    for monkey in monkeys.values():
        take_turn(monkey)
    # print(f'round {i}')


# print results
for i in range(len(monkeys.values())):
    print(f'Monkey {i}: {monkeys[i].items}')

print()
for i in range(len(monkeys.values())):
    print(f'Monkey {i} inspected {monkeys[i].inspects} items')

print()
inspects = []
for monkey in monkeys.values():
    inspects.append(monkey.inspects)

inspects.sort(reverse=True)
business = inspects[0] * inspects[1]
print(f'Monkey business level: {business}')