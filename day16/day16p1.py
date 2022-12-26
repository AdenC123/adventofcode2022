from collections import namedtuple
import re

filename = 'test.txt'
minutes = 30
start_valve = 'AA'
print_every = 100000

Valve = namedtuple('Valve', 'fl exits opened')
start_valves = {}
# 'AA': Valve(0, ('DD', 'II', 'BB'))


def parse_file():
    with open(filename) as f:
        for line in f:
            names = re.findall(r'[A-Z][A-Z]', line)
            fl = int(re.findall(r'\d+', line)[0])
            start_valves[names[0]] = Valve(fl, tuple(names[1:]), False)


parse_file()
Node = namedtuple('Node', 'valves current_valve minute pressure')


def print_state(checked, pressure):
    print(f'\rChecked {checked} nodes, max pressure is {pressure}')


def solve():
    # start at valve AA with 30 mins remaining and 0 pressure
    # valves dict keeps track of valve states
    wl = [Node(start_valves, 'AA', 30, 0)]
    max_pressure = 0
    nodes_checked = 0
    while wl:
        # print progress
        nodes_checked += 1
        if nodes_checked % print_every == 0:
            print(f'\rChecked {nodes_checked} nodes, '
                  f'max pressure so far is {max_pressure}', end='')

        node = wl.pop()
        valve = node.valves[node.current_valve]

        # trivial case: no minutes left
        if node.minute == 0:
            max_pressure = max(node.pressure, max_pressure)

        else:
            # try opening the valve
            if not valve.opened:
                new_valve = Valve(valve.fl, valve.exits, True)
                new_dict = node.valves.copy()
                new_dict[node.current_valve] = new_valve

                new_pressure = node.pressure + (node.minute * valve.fl)

                new_node = Node(new_dict, node.current_valve,
                                node.minute - 1, new_pressure)
                wl.append(new_node)

            # try moving to all exits
            for ex in valve.exits:
                new_node = Node(node.valves, ex,
                                node.minute - 1, node.pressure)
                wl.append(new_node)

    return max_pressure


max_pressure = solve()
print(f'Final max pressure: {max_pressure}')
