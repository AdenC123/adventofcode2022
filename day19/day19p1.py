from collections import namedtuple
import re

Blueprint = namedtuple('Blueprint', 'ore_from_ore clay_from_ore '
                                    'obsidian_from_ore obsidian_from_clay '
                                    'geode_from_ore geode_from_obsidian')
# Robots = namedtuple('Robots', 'ore clay obsidian geode')
# Resources = namedtuple('Resources', 'ore clay obsidian geode')
Node = namedtuple('Node', 'minute resources robots')

FILENAME = 'test.txt'
MAX_MINUTES = 24


def parse_file(filename):
    blueprints = {}
    with open(filename) as f:
        for line in f:
            nums = list(map(int, re.findall(r'\d+', line)))
            i = nums.pop(0)
            blueprints[i] = Blueprint(*nums)
    return blueprints


def collect_resources(robots, resources):
    # modifies resources
    for obj in robots.keys():
        resources[obj] += robots[obj]
    return resources


def next_nodes(node, bp):
    new_minute = node.minute + 1
    robots = node.robots
    resources = node.resources
    result = []

    # don't build
    new_resources = resources.copy()
    collect_resources(robots, new_resources)
    result.append(Node(new_minute, new_resources, robots))

    # build ore robot
    if resources['ore'] >= bp.ore_from_ore:
        new_robots = robots.copy()
        new_resources = resources.copy()
        new_resources['ore'] -= bp.ore_from_ore
        collect_resources(robots, new_resources)
        new_robots['ore'] += 1
        result.append(Node(new_minute, new_resources, new_robots))

    # build clay robot
    if resources['ore'] >= bp.clay_from_ore:
        new_robots = robots.copy()
        new_resources = resources.copy()
        new_resources['ore'] -= bp.clay_from_ore
        collect_resources(robots, new_resources)
        new_robots['clay'] += 1
        result.append(Node(new_minute, new_resources, new_robots))

    # build obsidian robot
    if resources['ore'] >= bp.obsidian_from_ore and \
            resources['clay'] >= bp.obsidian_from_clay:
        new_robots = robots.copy()
        new_resources = resources.copy()
        new_resources['ore'] -= bp.obsidian_from_ore
        new_resources['clay'] -= bp.obsidian_from_clay
        collect_resources(robots, new_resources)
        new_robots['obsidian'] += 1
        result.append(Node(new_minute, new_resources, new_robots))

    # build geode robot
    if resources['ore'] >= bp.geode_from_ore and \
            resources['obsidian'] >= bp.geode_from_obsidian:
        new_robots = robots.copy()
        new_resources = resources.copy()
        new_resources['ore'] -= bp.geode_from_ore
        new_resources['obsidian'] -= bp.geode_from_obsidian
        collect_resources(robots, new_resources)
        new_robots['geode'] += 1
        result.append(Node(new_minute, new_resources, new_robots))

    return result


def max_geodes(bp):
    start_robots = {'ore': 1, 'clay': 0, 'obsidian': 0, 'geode': 0}
    start_resources = {'ore': 0, 'clay': 0, 'obsidian': 0, 'geode': 0}
    wl = [Node(1, start_resources, start_robots)]
    rsf = 0
    last_minute = 1

    while wl:
        node = wl.pop()

        if node.minute != last_minute:
            last_minute = node.minute
            print(f'\rminute {last_minute}', end='')

        # base case
        if node.minute > MAX_MINUTES:
            rsf = max(rsf, node.resources['geode'])
        else:
            wl = next_nodes(node, bp) + wl

    return rsf


def main():
    result = 0
    blueprints = parse_file(FILENAME)
    for i in blueprints.keys():
        mg = max_geodes(blueprints[i])
        print(f'Quality level of blueprint {i} is {mg}')
        result += i * mg
    print(f'Final result: {result}')


if __name__ == '__main__':
    main()
