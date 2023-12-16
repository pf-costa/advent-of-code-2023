import heapq
from aocd import submit, get_data
import operator
import math
import itertools
from queue import PriorityQueue
from collections import deque


data = get_data(day=11, year=2023)


# Manhattan distance between two points
def manhattan_distance(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])


def get_total_distance(factor=1):
    galaxy = []

    for line in data.split("\n"):
        row = list(line)
        galaxy.append(row)

    # Get all the planets
    planets = []

    for i, row in enumerate(galaxy):
        for j, col in enumerate(row):
            if col == "#":
                galaxy[i][j] = str(len(planets))
                planets.append([i, j])

    # Get expandable rows
    target_rows_indexes = [
        i for i, row in enumerate(galaxy) if row.count(".") == len(row)
    ]

    target_column_indexes = [
        column
        for column in range(0, len(galaxy[0]) - 1)
        if all(row[column] == "." for row in galaxy)
    ]

    # Expand the galaxy
    for i in reversed(target_rows_indexes):
        affected_planets = [planet for planet in planets if planet[0] > i]
        for planet in affected_planets:
            planet[0] += factor

    for column in reversed(target_column_indexes):
        affected_planets = [planet for planet in planets if planet[1] > column]
        for planet in affected_planets:
            planet[1] += factor

    for i, row in enumerate(galaxy):
        for j, col in enumerate(row):
            if col == "#":
                galaxy[i][j] = str(len(planets))
                planets.append((i, j))

    # For all columns that contain all the character .
    planet_combinations = list(itertools.combinations(range(0, len(planets)), 2))
    total = 0

    for i, pair in enumerate(planet_combinations):
        [planet1, planet2] = pair

        coord1 = planets[planet1]
        coord2 = planets[planet2]

        total += manhattan_distance(coord1, coord2)

    return total


submit(part=1, day=11, year=2023, answer=get_total_distance())
submit(part=2, day=11, year=2023, answer=get_total_distance(1000000 - 1))
