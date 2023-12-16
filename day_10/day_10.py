from aocd import submit, get_data
import operator
import shapely.geometry

data = get_data(day=10, year=2023)

direction_changes = {
    "|": lambda dir: dir,
    "-": lambda dir: dir,
    "L": lambda dir: dir[::-1],
    "J": lambda dir: tuple(x * -1 for x in dir[::-1]),
    "7": lambda dir: dir[::-1],
    "F": lambda dir: tuple(x * -1 for x in dir[::-1]),
}


def change_direction(direction, pipe):
    return direction_changes[pipe](direction)


assert change_direction((1, 0), "|") == (1, 0)
assert change_direction((0, 1), "-") == (0, 1)
assert change_direction((1, 0), "L") == (0, 1)
assert change_direction((0, -1), "L") == (-1, 0)
assert change_direction((0, 1), "J") == (-1, 0)
assert change_direction((1, 0), "J") == (0, -1)
assert change_direction((-1, 0), "7") == (0, -1)
assert change_direction((0, 1), "7") == (1, 0)
assert change_direction((0, -1), "F") == (1, 0)
assert change_direction((-1, 0), "F") == (0, 1)

# Parse the data and fill the matrix
matrix = []
for line in data.split("\n"):
    row = list(line)
    matrix.append(row)


def get_current_position():
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if col == "S":
                return (i, j)


def get_next_position(position, direction):
    return tuple(map(operator.add, position, direction))


def perform_loop(on_cell):
    initial_position = get_current_position()

    next_position = None
    position = initial_position

    # Hardcoded initial direction
    # Just move!
    direction = (1, 0)

    while True:
        next_position = get_next_position(position, direction)
        position = next_position
        cell = matrix[next_position[0]][next_position[1]]

        if cell == "S":
            break

        direction = change_direction(direction, cell)
        on_cell(position)


def solve1():
    steps = 1

    def on_cell(position):
        nonlocal steps
        steps += 1

    perform_loop(on_cell)

    return steps / 2


def solve2():
    VISITED = " "
    polygon = []

    def on_cell(position):
        matrix[position[0]][position[1]] = VISITED
        polygon.append(position)

    perform_loop(on_cell)

    tiles = 0
    polygon = shapely.geometry.Polygon([(b, a) for (a, b) in polygon])

    # Chars in first or last row are never surrounded by spaces
    for row_index, row in enumerate(matrix):
        # Get chars that are surrounded by spaces
        row = "".join(row)
        print(row_index)

        for col_index, cell in enumerate(row):
            if cell == VISITED:
                continue

            point = shapely.geometry.Point((col_index, row_index))

            if point.within(polygon):
                tiles += 1
                matrix[row_index][col_index] = "X"

    return tiles


submit(part=1, day=10, year=2023, answer=solve1())
submit(part=2, day=10, year=2023, answer=solve2())
