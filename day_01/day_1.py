from aocd import submit, data
import re

NUMBERS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def get_number(number: str):
    if str.isnumeric(number):
        return number

    return str(NUMBERS.index(number) + 1)


def solve(regex: str):
    items = [re.findall(regex, line) for line in data.split("\n")]
    items2 = [int(get_number(n[0]) + get_number(n[-1])) for n in items]

    return sum(items2)


solution1 = solve(r"\d")
# TIL: Use positive lookahead to find the numbers
solution2 = solve(rf"(?=(\d|{'|'.join(NUMBERS)}))")

submit(part=1, day=1, year=2023, answer=solution1)
submit(part=2, day=1, year=2023, answer=solution2)
