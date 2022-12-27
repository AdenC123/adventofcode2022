from collections import namedtuple
import re

# only care about valves with flow rate > 0, rest are not important
# travel between important valves, each travel costs a number of minutes

# when at a valve, try opening the valve and try going to all other important valves
# that can be reached within time limit

# don't go back to the important valve we were just at
# initially, just go to all important valves with costs from AA

# need to precompute shortest distances to all valves from all other valves
# do bfs for every important valve


filename = 'input.txt'
total_minutes = 30
start_valve = 'AA'
# print_every = 1

Valve = namedtuple('Valve', 'fl exits')
Node = namedtuple('Node', 'to_visit last_valve minute pressure')


def get_all_valves():
    result = {}
    with open(filename) as f:
        for line in f:
            names = re.findall(r'[A-Z][A-Z]', line)
            fl = int(re.findall(r'\d+', line)[0])
            result[names[0]] = Valve(fl, tuple(names[1:]))
    return result


def get_important_valves():
    # need start valve for distance dictionary, remove it later
    result = [start_valve]
    for valve_name in all_valves.keys():
        if all_valves[valve_name].fl > 0:
            result.append(valve_name)
    return result


def shortest_path(from_valve, to_valve):
    visited = []
    queue = [[from_valve]]
    while queue:
        path = queue.pop(0)
        valve = path[-1]
        if valve == to_valve:
            return path
        elif valve in visited:
            pass
        else:
            visited.append(valve)
            for ex in all_valves[valve].exits:
                new_path = path + [ex]
                queue.append(new_path)
    raise Exception(f'no path found from {from_valve} to {to_valve}')


def get_distances():
    result = {}
    for from_valve in important_valves:
        rest = important_valves.copy()
        rest.remove(from_valve)
        for to_valve in rest:
            distance = len(shortest_path(from_valve, to_valve)) - 1
            result[(from_valve, to_valve)] = distance
    return result


def print_state(checked, pressure):
    print(f'\rChecked {checked} nodes, max pressure is {pressure}')


def solve():
    # start leaving AA with 30 mins remaining and 0 pressure
    wl = [Node(important_valves, start_valve, total_minutes, 0)]
    max_pressure = 0
    # nodes_checked = 0
    while wl:
        # print progress
        # nodes_checked += 1
        # if nodes_checked % print_every == 0:
        #     print(f'\rChecked {nodes_checked} nodes, '
        #           f'max pressure so far is {max_pressure}', end='')

        node = wl.pop()

        new_nodes = []
        for to_valve in node.to_visit:
            dist = distances[(node.last_valve, to_valve)]
            # time taken to go there and open the valve
            new_mins = node.minute - dist - 1
            if new_mins >= 0:
                new_pressure = node.pressure + \
                               (new_mins * all_valves[to_valve].fl)
                new_to_visit = node.to_visit.copy()
                new_to_visit.remove(to_valve)
                new_node = Node(new_to_visit, to_valve, new_mins, new_pressure)
                new_nodes.append(new_node)
        if len(new_nodes) == 0:
            # trivial case: no more valid nodes
            max_pressure = max(node.pressure, max_pressure)
        else:
            wl += new_nodes

    return max_pressure


all_valves = get_all_valves()
important_valves = get_important_valves()
distances = get_distances()
# we only need AA for distances
important_valves.remove(start_valve)

final_max = solve()
print(f'\nFinal max pressure: {final_max}')
