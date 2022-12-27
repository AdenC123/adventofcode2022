from collections import namedtuple
import re

filename = 'input.txt'
minutes = 26
print_every = 1000000

Valve = namedtuple('Valve', 'fl exits opened')
Node = namedtuple('Node', 'valves current_valve last_valve'
                          ' elephant_current_valve elephant_last_valve'
                          ' minute pressure')

start_valves = {}
# 'AA': Valve(0, ('DD', 'II', 'BB'), False)


def parse_file():
    with open(filename) as f:
        for line in f:
            names = re.findall(r'[A-Z][A-Z]', line)
            fl = int(re.findall(r'\d+', line)[0])
            start_valves[names[0]] = Valve(fl, tuple(names[1:]), False)


def get_important_valves():
    result = []
    for valve_name in start_valves.keys():
        if start_valves[valve_name].fl > 0:
            result.append(valve_name)
    return result


def print_state(checked, pressure):
    print(f'\rChecked {checked} nodes, max pressure is {pressure}')


def all_open(valves):
    for valve in valves.keys():
        if valve in important_valves and not valves[valve].opened:
            return False
    return True


def solve():
    # start at valve AA with 30 mins remaining and 0 pressure
    # valves dict keeps track of valve states
    wl = [Node(start_valves, 'AA', 'AA', 'AA', 'AA', minutes, 0)]
    max_pressure = 0
    nodes_checked = 0
    while wl:
        # print progress
        nodes_checked += 1
        if nodes_checked % print_every == 0:
            print(f'\rChecked {nodes_checked} nodes, '
                  f'max pressure so far is {max_pressure}', end='')

        node = wl.pop()
        player_valve = node.valves[node.current_valve]

        # trivial case: no minutes left or all valves with fl > 0 open
        if node.minute == 0 or all_open(node.valves):
            max_pressure = max(node.pressure, max_pressure)

        else:
            # generate nodes for player
            player_nodes = []
            # try opening the valve
            # but not if it's flow rate is 0
            if not (player_valve.opened or player_valve.fl == 0):
                new_valve = Valve(player_valve.fl, player_valve.exits, True)
                new_dict = node.valves.copy()
                new_dict[node.current_valve] = new_valve

                new_pressure = node.pressure + ((node.minute - 1) * player_valve.fl)

                new_node = Node(new_dict, node.current_valve, node.current_valve,
                                node.elephant_current_valve, node.elephant_last_valve,
                                node.minute - 1, new_pressure)
                player_nodes.append(new_node)

            # try moving to all exits
            for ex in player_valve.exits:
                # but not the one we were just at or the one the elephant is at??
                if ex != node.last_valve and ex != node.elephant_current_valve:
                    new_node = Node(node.valves, ex, node.current_valve,
                                    node.elephant_current_valve, node.elephant_last_valve,
                                    node.minute - 1, node.pressure)
                    player_nodes.append(new_node)

            # now add all elephant moves for every player move
            if type(player_nodes) == list:
                for node in player_nodes:
                    elephant_valve = node.valves[node.elephant_current_valve]
                    # try opening the valve
                    # but not if it's flow rate is 0
                    if not (elephant_valve.opened or elephant_valve.fl == 0):
                        new_valve = Valve(elephant_valve.fl, elephant_valve.exits, True)
                        new_dict = node.valves.copy()
                        new_dict[node.elephant_current_valve] = new_valve

                        # minute has already passed, don't subtract
                        new_pressure = node.pressure + (node.minute * elephant_valve.fl)

                        new_node = Node(new_dict, node.current_valve, node.last_valve,
                                        node.elephant_current_valve, node.elephant_current_valve,
                                        node.minute, new_pressure)
                        wl.append(new_node)
                    # try moving to all exits
                    for ex in elephant_valve.exits:
                        # but not the one we were just at or the one the player is at??
                        if ex != node.elephant_last_valve and ex != node.current_valve:
                            new_node = Node(node.valves, node.current_valve, node.last_valve,
                                            ex, node.elephant_current_valve,
                                            node.minute, node.pressure)
                            wl.append(new_node)

    return max_pressure


parse_file()
important_valves = get_important_valves()
final_max = solve()
print(f'\nFinal max pressure: {final_max}')
