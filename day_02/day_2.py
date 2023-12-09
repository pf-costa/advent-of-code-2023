from aocd import submit, get_data
import re
from collections import defaultdict
from operator import mul
from functools import reduce

data = get_data(day=2, year=2023).split("\n")

MAX_CUBES = {"red": 12, "green": 13, "blue": 14}


def get_count(line):
    [count, color] = line.strip().split(" ")
    return {color: int(count)}


def is_valid(items):
    for item in items:
        for color, count in item.items():
            if count > MAX_CUBES[color]:
                return False

    return True


def get_sets():
    result = {}

    for line in data:
        [game, sets] = line.split(":")
        [id] = re.findall(r"\d+", game)

        cubes = [cubes for set in sets.split(";") for cubes in set.split(",")]
        items = [get_count(called) for called in cubes]

        result[id] = items

    return result


def solve2():
    sets = get_sets()
    total = 0

    for id in sets:
        colors = {}

        for item in sets[id]:
            # if not is_valid([item]):
            #     break

            for color, count in item.items():
                if color not in colors:
                    colors[color] = 0

                count = int(count)

                if count > colors[color]:
                    colors[color] = count

        total += reduce(mul, colors.values())

    return total


def solve1():
    ids = []
    sets = get_sets()

    for id in sets:
        if is_valid(sets[id]):
            ids.append(int(id))

    return sum(ids)

submit(part=1, day=2, year=2023, answer=solve1())
submit(part=2, day=2, year=2023, answer=solve2())
