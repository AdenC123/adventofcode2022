from collections import namedtuple
import re


filename = 'input.txt'
total_minutes = 26
start_valve = 'AA'
print_every = 10000

Valve = namedtuple('Valve', 'fl exits')
Node = namedtuple('Node', 'to_visit last_player_valve last_elephant_valve'
                          ' player_minutes elephant_minutes pressure')


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
    wl = [Node(important_valves, start_valve, start_valve,
               total_minutes, total_minutes, 0)]
    max_pressure = 0
    nodes_checked = 0
    while wl:
        # print progress
        nodes_checked += 1
        if nodes_checked % print_every == 0:
            print(f'\rChecked {nodes_checked} nodes, '
                  f'max pressure so far is {max_pressure}', end='')

        node = wl.pop()
        valid_player_valves = []
        valid_elephant_valves = []

        for to_valve in node.to_visit:
            # get next valid player valves
            dist = distances[(node.last_player_valve, to_valve)]
            new_player_mins = node.player_minutes - dist - 1
            if new_player_mins >= 0:
                valid_player_valves.append((to_valve, new_player_mins))

            # and next valid elephant valves
            dist = distances[node.last_elephant_valve, to_valve]
            new_elephant_mins = node.elephant_minutes - dist - 1
            if new_elephant_mins >= 0:
                valid_elephant_valves.append((to_valve, new_elephant_mins))

        if len(valid_player_valves) == 0 and len(valid_elephant_valves) == 0:
            # no more valid moves for either, end here
            max_pressure = max(node.pressure, max_pressure)
        elif len(valid_elephant_valves) == 0:
            # only move player
            for to_valve, new_mins in valid_player_valves:
                new_pressure = node.pressure + \
                               (new_mins * all_valves[to_valve].fl)
                new_to_visit = node.to_visit.copy()
                new_to_visit.remove(to_valve)
                new_node = Node(new_to_visit, to_valve, node.last_elephant_valve,
                                new_mins, 0, new_pressure)
                wl.append(new_node)
        elif len(valid_player_valves) == 0:
            # only move elephant
            for to_valve, new_mins in valid_elephant_valves:
                new_pressure = node.pressure + \
                               (new_mins * all_valves[to_valve].fl)
                new_to_visit = node.to_visit.copy()
                new_to_visit.remove(to_valve)
                new_node = Node(new_to_visit, node.last_player_valve, to_valve,
                                0, new_mins, new_pressure)
                wl.append(new_node)
        else:
            # both elephant and player have valid moves, do all combinations of both
            for player_valve, new_player_mins in valid_player_valves:
                for elephant_valve, new_elephant_mins in valid_elephant_valves:
                    # but don't have them go to the same place
                    if player_valve != elephant_valve:
                        new_pressure = node.pressure\
                                       + (new_player_mins * all_valves[player_valve].fl)\
                                       + (new_elephant_mins * all_valves[elephant_valve].fl)
                        new_to_visit = node.to_visit.copy()
                        new_to_visit.remove(player_valve)
                        new_to_visit.remove(elephant_valve)
                        new_node = Node(new_to_visit, player_valve, elephant_valve,
                                        new_player_mins, new_elephant_mins, new_pressure)
                        wl.append(new_node)

    return max_pressure


all_valves = get_all_valves()
important_valves = get_important_valves()
distances = get_distances()
# we only need AA for distances
important_valves.remove(start_valve)

final_max = solve()
print(f'\nFinal max pressure: {final_max}')
