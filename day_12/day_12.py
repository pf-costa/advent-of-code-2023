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


def is_valid(line, groups, is_complete=True):
    regex = r"#+" if is_complete else r"([#?]+)"
    matches = list(re.finditer(regex, line))

    if is_complete and len(matches) != len(groups):
        return False

    if not is_complete and len(matches) > len(groups):
        matches = matches[: len(groups)]

    for i, match in enumerate(matches):
        length = match.end() - match.start()

        if is_complete and length != groups[i]:
            return False

        if length < groups[i]:
            return False

    return True


def get_possibilities(line, groups):
    total = 0

    if "?" not in line:
        if is_valid(line, groups):
            return 1
        else:
            return 0

    index = line.index("?")

    line2 = line[:index] + "." + line[index + 1 :]
    total += get_possibilities(line2, groups)

    line2 = line[:index] + "#" + line[index + 1 :]
    # next_char = line[index + 1] if index + 1 < len(line2) else None

    # if next_char == "#":
    #     if not is_valid(line2, groups, False):
    #         return total

    total += get_possibilities(line2, groups)
    return total


# 1
# 4
# 1
# 1
# 4
# 10

# for row in rows:
#     print(get_possibilities(*row))

# print(get_possibilities(*rows[2]))

tot = 0

print("Computing for", len(rows), "rows")

for i, row in enumerate(rows):
    tot += get_possibilities(*row)
    print("Computed row", i)

print("total", tot)

part1 = sum(get_possibilities(*l) for l in rows)
# print(part1)

# 6986 - too low

# submit(part=1, day=12, year=2023, answer=get_total_distance())
# submit(part=2, day=12, year=2023, answer=get_total_distance(1000000 - 1))
