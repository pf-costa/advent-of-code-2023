from functools import reduce
from aocd import submit, get_data
import operator
import math
from collections import defaultdict
from functools import cmp_to_key
import re

data = get_data(day=9, year=2023)

sequences = [list(map(int, l.split())) for l in data.split("\n")]


def predict_sequence(values, last_value=0):
    next_values = []

    for i in range(0, len(values) - 1):
        next_values.append(values[i + 1] - values[i])

    all_zeroes = all(num == 0 for num in next_values)

    if not all_zeroes:
        result = predict_sequence(next_values, values[-1])
        return last_value + result

    return values[-1] + last_value


def back_in_time(values, last_value=None):
    next_values = []

    for i in range(0, len(values) - 1):
        next_values.append(values[i + 1] - values[i])

    all_zeroes = all(num == 0 for num in next_values)

    if not all_zeroes:
        result = back_in_time(next_values, values[0])

        if last_value is None:
            return result

        return last_value - result

    return last_value - values[0]


def solve1():
    return sum(map(predict_sequence, sequences))


def solve2():
    return sum(map(back_in_time, sequences))


submit(part=1, day=9, year=2023, answer=solve1())
submit(part=2, day=9, year=2023, answer=solve2())
