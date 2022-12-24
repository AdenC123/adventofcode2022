from dataclasses import dataclass


@dataclass
class Pair:
    left: list | int
    right: list | int


filename = 'input.txt'
pairs = []
with open(filename) as f:
    lines = f.readlines()

while lines:
    pairs.append(Pair(eval(lines.pop(0).strip()),
                      eval(lines.pop(0).strip())))
    lines.pop(0)


def valid(pair):
    left = pair.left
    right = pair.right

    if type(left) == list and type(right) == list:
        while left:
            if right:
                result = valid(Pair(left.pop(0), right.pop(0)))
                if result is not None:
                    return result
            else:
                # left has elements but right does not
                return False
        # left does not exist
        if right:
            return True
        else:
            return None

    elif type(left) == int and type(right) == int:
        if left < right:
            return True
        elif left > right:
            return False
        else:
            return None

    elif type(left) == int:
        return valid(Pair([left], right))

    else:
        return valid(Pair(left, [right]))


valids = []
for i in range(len(pairs)):
    if valid(pairs[i]):
        valids.append(i+1)

print(valids)
print(f'Sum: {sum(valids)}')
