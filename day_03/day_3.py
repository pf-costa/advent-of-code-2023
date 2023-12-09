from aocd import submit, get_data
import re
from collections import defaultdict
from operator import mul
from functools import reduce
from itertools import groupby

data = get_data(day=3, year=2023).split("\n")

# Create a matrix
matrix = [list(row) for row in data]
rows = len(matrix)
cols = len(matrix[0])

NEIGHBORS = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]


def is_symbol(symbol):
    return symbol != "." and not symbol.isdigit()


def get_valid_neigbors(func):
    def validate(target_row, target_column):
        # for the current element, check all neighbors and check if they are symbols
        for neighbor in NEIGHBORS:
            row = target_row + neighbor[0]
            col = target_column + neighbor[1]

            if row < 0 or row >= rows:
                continue

            if col < 0 or col >= cols:
                continue

            neighbor_element = matrix[row][col]

            if func(neighbor_element):
                yield (row, col)

    return validate


def solve1():
    numbers = []
    has_symbol_neighbor = get_valid_neigbors(is_symbol)

    for i in range(rows):
        for match in re.finditer(r"\d+", data[i]):
            start = match.start()
            end = match.end()
            number = int(match.group())

            for j in range(start, end):
                element = matrix[i][j]

                if element == ".":
                    continue

                if is_symbol(element):
                    continue

                if any(has_symbol_neighbor(i, j)):
                    numbers.append(number)
                    break

    return sum(numbers)


def solve2():
    numbers = []
    has_number_neighbors = get_valid_neigbors(lambda char: char.isdigit())
    total = 0

    for i in range(rows):
        for match in re.finditer(r"\*", data[i]):
            column = match.start()

            valid_neighbors = list(has_number_neighbors(i, column))
            numbers = []

            # Group all the valid neighbors by row
            for row, group in groupby(valid_neighbors, key=lambda x: x[0]):
                columns = list(map(lambda x: x[1], group))

                # Get the numbers from the row
                for m in re.finditer(r"\d+", data[row]):
                    # Only if the start and match are in the columns
                    # consider the number to be valid
                    if any(m.start() <= col <= m.end() for col in columns):
                        numbers.append(int(m.group()))

            if len(numbers) >= 2:
                total += reduce(mul, numbers)

    return total


submit(part=1, day=3, year=2023, answer=solve1())
submit(part=2, day=3, year=2023, answer=solve2())
