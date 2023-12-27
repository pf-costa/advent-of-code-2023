import heapq
from aocd import submit, get_data
import operator
import math
import itertools
import re

data = get_data(day=12, year=2023)

# data = """???.### 1,1,3
# .??..??...?##. 1,1,3
# ?#?#?#?#?#?#?#? 1,3,1,6
# ????.#...#... 4,1,1
# ????.######..#####. 1,6,5
# ?###???????? 3,2,1"""

rows = []

for line in data.split("\n"):
    info, numbers = line.split(" ")
    numbers = [int(n) for n in numbers.split(",")]
    rows.append((info, numbers))


memory = {}


def memoize(f):
    def inner(line, groups):
        key = (line, *groups)

        if key not in memory:
            memory[key] = f(line, groups)

        return memory[key]

    return inner


@memoize
def count_possibilities(line, groups):
    total = 0

    # If there are no more characters
    if len(line) == 0:
        return 1 if len(groups) == 0 else 0

    # If there are no more groups
    if len(groups) == 0:
        # And there are no more #'s
        return 0 if "#" in line else 1

    # Replace with ? with .
    if line[0] in ".?":
        # In this case we also "swap" the ? with a .
        total += count_possibilities(line[1:], groups)

    if line[0] in "#?":
        if (
            # If the current group length is in between the length of the line
            groups[0] <= len(line)
            # Remember that a group is always separated by a .
            and "." not in line[: groups[0]]
            # And the group is valid. The length matches of the next character is not a #
            and (groups[0] == len(line) or line[groups[0]] != "#")
        ):
            total += count_possibilities(line[groups[0] + 1 :], groups[1:])

    return total


part1 = sum(count_possibilities(*l) for l in rows)

folded_rows = [("?".join([r] * 5), g * 5) for (r, g) in rows]
part2 = sum(count_possibilities(*l) for l in folded_rows)

submit(part=1, day=12, year=2023, answer=part1)
submit(part=2, day=12, year=2023, answer=part2)
