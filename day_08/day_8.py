from functools import reduce
from aocd import submit, get_data
import operator
import math
from collections import defaultdict
from functools import cmp_to_key
import re

data = get_data(day=8, year=2023)

[instructions, lines] = data.split("\n\n")
nodes = {}

for l in lines.split("\n"):
    [node, left, right] = re.findall(r"(\w+)", l.split("\n")[0])
    nodes[node] = (left, right)

START_NODE = "AAA"
END_NODE = "ZZZ"


def get_steps(node_key, end_condition):
    current_node_key = node_key
    steps = 0

    while True:
        for instruction in instructions:
            node = nodes[current_node_key]
            current_node_key = node[0] if instruction == "L" else node[1]
            steps += 1

            if end_condition(current_node_key):
                return steps


def solve1():
    return get_steps(START_NODE, lambda x: x == END_NODE)


def get_nodes(pred):
    return map(lambda n: n[0], filter(pred, nodes.items()))


def lcm(numbers):
    return reduce(lambda a, b: abs(a * b) // math.gcd(a, b), numbers)


def solve2():
    current_nodes = list(get_nodes(lambda x: "A" in x[0]))
    total_steps = []

    for n in current_nodes:
        total_steps.append(get_steps(n, lambda x: "Z" in x))

    return lcm(total_steps)


submit(part=1, day=8, year=2023, answer=solve1())
submit(part=2, day=8, year=2023, answer=solve2())
