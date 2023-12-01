import re
from collections import namedtuple, deque
from typing import Dict, List

# STRUCTURES
Blueprint = namedtuple("Blueprint", "ore_ore_cost clay_ore_cost "
                                    "obsidian_ore_cost obsidian_clay_cost "
                                    "geode_ore_cost geode_obsidian_cost")
Node = namedtuple("Node", "minute robots resources")
Robots = namedtuple("Robots", "ore clay obsidian geode")
Resources = namedtuple("Resources", "ore clay obsidian geode")

# CONSTANTS
FILENAME = "test.txt"
MAX_MINUTES = 24

# GLOBALS
blueprints: Dict[int, Blueprint] = {}

with open(FILENAME) as f:
    for line in f:
        nums = list(map(int, re.findall(r'\d+', line)))
        id = int(nums.pop(0))
        blueprints[id] = Blueprint(*nums)


def next_nodes(node, bp) -> List[Node]:
    # advance minutes, all robots produce
    new_minute = node.minute + 1
    produced_resources: List[Resources] = [node.resources[i] + node.robots[i] for i in range(4)]

    # all helpful robot productions
    # just build a geode robot if we have enough resources
    if node.resources.ore >= bp.geode_ore_cost and node.resources.obsidian >= bp.geode_obsidian_cost:
        new_resources = produced_resources.copy()
        new_resources[0] -= bp.geode_ore_cost
        new_resources[2] -= bp.geode_obsidian_cost
        new_robots = list(node.robots)
        new_robots[3] += 1
        return [Node(new_minute, Robots(*new_robots), Resources(*new_resources))]
    # build nothing
    new_nodes = [Node(new_minute, node.robots, Resources(*produced_resources))]
    # build a ore robot if we have enough ore and we haven't hit the max
    max_ore_robots = max(bp.ore_ore_cost, bp.clay_ore_cost, bp.obsidian_ore_cost, bp.geode_ore_cost)
    if node.resources.ore >= bp.ore_ore_cost and node.robots.ore < max_ore_robots:
        new_resources = produced_resources.copy()
        new_resources[0] -= bp.ore_ore_cost
        new_robots = list(node.robots)
        new_robots[0] += 1
        new_nodes.append(Node(new_minute, Robots(*new_robots), Resources(*new_resources)))
    # build a clay robot if we have enough ore and we haven't hit the max
    if node.resources.ore >= bp.clay_ore_cost and node.robots.clay < bp.obsidian_clay_cost:
        new_resources = produced_resources.copy()
        new_resources[0] -= bp.clay_ore_cost
        new_robots = list(node.robots)
        new_robots[1] += 1
        new_nodes.append(Node(new_minute, Robots(*new_robots), Resources(*new_resources)))
    # build a obsidian robot if we have enough ore and clay and we haven't hit the max
    if node.resources.ore >= bp.obsidian_ore_cost and node.resources.clay >= bp.obsidian_clay_cost \
            and node.robots.obsidian < bp.geode_obsidian_cost:
        new_resources = produced_resources.copy()
        new_resources[0] -= bp.obsidian_ore_cost
        new_resources[1] -= bp.obsidian_clay_cost
        new_robots = list(node.robots)
        new_robots[2] += 1
        new_nodes.append(Node(new_minute, Robots(*new_robots), Resources(*new_resources)))
    return new_nodes


def worse_than_best(node, rsf):
    """Returns true iff the node cannot produce more than rsf geodes by building a geode robot every minute."""
    geodes = node.resources.geode
    robots = node.robots.geode
    for i in range(node.minute, MAX_MINUTES):
        geodes += robots
        robots += 1
    return geodes < rsf


def max_geodes(bp: Blueprint) -> int:
    # create initial node with one ore robot
    start = Node(0, Robots(1, 0, 0, 0), Resources(0, 0, 0, 0))
    todo = deque()
    todo.append(start)
    # BFS with all possible (helpful) actions
    rsf = 0
    max_minute = 0
    while todo:
        curr: Node = todo.popleft()
        if curr.minute > max_minute:
            print("Minute {}".format(curr.minute))
            print("Max Geodes: {}".format(rsf))
            max_minute = curr.minute
        if curr.minute > MAX_MINUTES:
            rsf = max(rsf, curr.resources.geode)
        elif not worse_than_best(curr, rsf):
            todo.extend(next_nodes(curr, bp))
    return rsf


def part1() -> str:
    return str(max_geodes(blueprints[1]))


def part2() -> str:
    return ""


print("Part 1: " + part1())
print("Part 2: " + part1())
