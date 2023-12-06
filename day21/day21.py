from sympy import solve, parse_expr, Eq


# STRUCTURES


# GLOBALS


# MAIN
def get_number(name, monkeys):
    expr = monkeys[name]
    if expr.isdigit():
        return int(expr)
    val1 = get_number(expr[0:4], monkeys)
    val2 = get_number(expr[7:], monkeys)
    op = expr[5]
    result = eval('{} {} {}'.format(val1, op, val2))
    monkeys[name] = result
    return result


def part1(lines) -> int:
    monkeys = {}
    for line in lines:
        monkeys[line[0:4]] = line[6:].strip()
    return get_number('root', monkeys)


def make_eqn(name, monkeys):
    if name == 'humn':
        return 'x'
    expr = monkeys[name]
    if expr.isdigit():
        return expr
    left_eqn = make_eqn(monkeys[name][0:4], monkeys)
    right_eqn = make_eqn(monkeys[name][7:], monkeys)
    op = expr[5]
    result = '({} {} {})'.format(left_eqn, op, right_eqn)
    return result


def part2(lines) -> int:
    monkeys = {}
    for line in lines:
        monkeys[line[0:4]] = line[6:].strip()
    left_eqn = make_eqn(monkeys['root'][0:4], monkeys)
    right_eqn = make_eqn(monkeys['root'][7:], monkeys)
    # eqn = '{} = {}'.format(left_eqn, right_eqn)
    left_expr = parse_expr(left_eqn)
    right_expr = parse_expr(right_eqn)
    return solve(Eq(left_expr, right_expr))[0]


def main():
    with open("test.txt") as f:
        lines = f.readlines()
        # print("Part 1 Test: " + str(part1(lines)))
        print("Part 2 Test: " + str(part2(lines)))
    with open("input.txt") as f:
        lines = f.readlines()
        # print("Part 1 Input: " + str(part1(lines)))
        print("Part 2 Input: " + str(part2(lines)))


if __name__ == '__main__':
    main()
