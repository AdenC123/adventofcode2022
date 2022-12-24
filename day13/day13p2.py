filename = 'input.txt'
packets = []

with open(filename) as f:
    for line in f:
        if line.strip():
            packets.append(eval(line.strip()))


def valid(left, right):
    if type(left) == list and type(right) == list:
        left = left.copy()
        right = right.copy()
        while left:
            if right:
                result = valid(left.pop(0), right.pop(0))
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
        return valid([left], right)

    else:
        return valid(left, [right])


def qsort(lst):
    if len(lst) < 2:
        return lst
    else:
        pivot = lst[0]
        before = [p for p in lst if valid(p, pivot)]
        after = [p for p in lst if valid(pivot, p)]
        return qsort(before) + [pivot] + qsort(after)


packets.append([[2]])
packets.append([[6]])

packets = qsort(packets)

divider2 = packets.index([[2]]) + 1
divider6 = packets.index([[6]]) + 1

print(f'Divider 2: {divider2}')
print(f'Divider 6: {divider6}')
print(f'Answer: {divider6 * divider2}')
