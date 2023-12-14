from functools import reduce
from aocd import submit, get_data
import operator
import math

data = get_data(day=6, year=2023)
races = []
lines = data.split("\n")


def get_numbers(line):
    return list(map(int, line.split(":")[1].lstrip().rsplit()))


times = get_numbers(lines[0])
distances = get_numbers(lines[1])


def solve1():
    ways = []

    for i, time in enumerate(times):
        print("time", time)

        wins = 0

        for hold in range(0, time + 1):
            remaining_time = time - hold

            distance = remaining_time * hold

            if distances[i] < distance:
                wins += 1

        ways.append(wins)

    return reduce(operator.mul, ways)


def solve2():
    # Since the values have a normal distribution
    # We can start by the middle value
    ways = 0

    time = int(reduce(lambda acc, n: acc + str(n), map(str, times), ""))
    distance = int(reduce(lambda acc, n: acc + str(n), map(str, distances), ""))
    hold = math.floor(time / 2)

    is_odd = time % 2 != 0

    if is_odd:
        ways += 1

    while True:
        remaining_time = time - hold

        if remaining_time * hold > distance:
            # Since this is a normal distribution we know that
            # time - hold is true for time + hold
            ways += 2
            hold -= 1
            continue

        break

    return ways - 1


submit(part=1, day=6, year=2023, answer=solve1())
submit(part=2, day=6, year=2023, answer=solve2())
