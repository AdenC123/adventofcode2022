from collections import namedtuple
import re

filename = 'input.txt'
minutes = 30
start_valve = 'AA'
print_every = 1000000

Valve = namedtuple('Valve', 'fl exits opened')
Node = namedtuple('Node', 'valves current_valve last_valve'
                          ' minute pressure')

start_valves = {}
# 'AA': Valve(0, ('DD', 'II', 'BB'))


def parse_file():
    with open(filename) as f:
        for line in f:
            names = re.findall(r'[A-Z][A-Z]', line)
            fl = int(re.findall(r'\d+', line)[0])
            start_valves[names[0]] = Valve(fl, tuple(names[1:]), False)


parse_file()


def print_state(checked, pressure):
    print(f'\rChecked {checked} nodes, max pressure is {pressure}')


def solve():
    # start at valve AA with 30 mins remaining and 0 pressure
    # valves dict keeps track of valve states
    wl = [Node(start_valves, 'AA', 'AA', 30, 0)]
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
            # but not if it's flow rate is 0
            if not (valve.opened or valve.fl == 0):
                new_valve = Valve(valve.fl, valve.exits, True)
                new_dict = node.valves.copy()
                new_dict[node.current_valve] = new_valve

                new_pressure = node.pressure + ((node.minute - 1) * valve.fl)

                new_node = Node(new_dict, node.current_valve,
                                node.current_valve,
                                node.minute - 1, new_pressure)
                wl.append(new_node)

            # try moving to all exits
            for ex in valve.exits:
                # but not the one we were just at
                if ex != node.last_valve:
                    new_node = Node(node.valves, ex, node.current_valve,
                                    node.minute - 1, node.pressure)
                    wl.append(new_node)

    return max_pressure


final_max = solve()
print(f'\nFinal max pressure: {final_max}')
