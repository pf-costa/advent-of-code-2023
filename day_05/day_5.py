from aocd import submit, get_data
import math

data = get_data(day=5, year=2023)

# data = """seeds: 79 14 55 13

# seed-to-soil map:
# 50 98 2
# 52 50 48

# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15

# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4

# water-to-light map:
# 88 18 7
# 18 25 70

# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13

# temperature-to-humidity map:
# 0 69 1
# 1 0 69

# humidity-to-location map:
# 60 56 37
# 56 93 4"""

data = data.split("\n\n")
seeds = []
maps = []

for i, item in enumerate(data):
    if i == 0:
        seeds = map(int, item.split(":")[1].split())
        continue

    m = [map(int, i.split()) for i in item.split("\n")[1:]]

    # Obtain the limits for each map
    maps.append(m)


def convert_seed_with_sub_map(seed, m):
    [end, start, range] = m

    if not start <= seed <= start + range:
        return None

    position = seed - start
    return end + position


def convert_seed(seed):
    current = seed

    for m in maps:
        for sub_map in m:
            result = convert_seed_with_sub_map(current, sub_map)

            if result is not None:
                current = result
                break

    return current


def solve1():
    lowest = None

    for seed in seeds:
        current = convert_seed(seed)

        if lowest is None or current < lowest:
            lowest = current

    return lowest


# def solve2_temp():
#     lowest = None

#     for i in range(0, len(seeds), 2):
#         # According to the previous computed limits, we need to avoid to perform redundant computations.
#         # For each interval select the least number
#         start = seeds[i]
#         end = seeds[i] + seeds[i + 1]

#         # Split by ranges
#         INCREMENT = 10000
#         cursor = start + INCREMENT

#         print("start", start, "end", end)

#         # This is the guaranteed minimum for the current range
#         current = convert_seed(start)
#         current_temp = current

#         if lowest is None:
#             lowest = current

#         if lowest < current:
#             lowest = current
#             continue

#         while cursor < end:
#             temp = convert_seed(cursor)

#             # Find the first number that is not linear with the previous one
#             if temp - INCREMENT == current_temp:
#                 cursor += INCREMENT
#                 current_temp = temp
#                 continue

#             # We found an anomaly in the sequence
#             cursor -= INCREMENT
#             current_temp = convert_seed(cursor)

#             for i in range(1, INCREMENT):
#                 temp = convert_seed(cursor + i)

#                 if temp - i == current_temp:
#                     continue

#                 cursor += i
#                 current_temp = temp

#                 if lowest > temp:
#                     lowest = temp

#                 break

#         cursor -= INCREMENT

#         for i in range(0, len(cursor)):
#             temp = convert_seed(cursor + i)

#             if lowest > temp:
#                 lowest = temp

#     return min(lowest)


def solve2():
    lowest = None

    for i in range(0, len(seeds), 2):
        start = seeds[i]
        end = seeds[i] + seeds[i + 1]

        print("Running", start, end)

        while start < end:
            temp = convert_seed(start)
            start += 1

            if lowest is None or temp < lowest:
                lowest = temp

    return lowest


print(solve2())

# submit(part=2, day=5, year=2023, answer=solve2())
