from aocd import submit, get_data

data = get_data(day=5, year=2023)

data = data.split("\n\n")
seeds = []
maps = []

for i, item in enumerate(data):
    if i == 0:
        seeds = list(map(int, item.split(":")[1].split()))
        continue

    m = [list(map(int, i.split())) for i in item.split("\n")[1:]]

    # Obtain the limits for each map
    maps.append(m)


def convert_seed_with_sub_map(seed, m):
    end, start, r = m

    if not start <= seed <= start + r:
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


def solve2():
    lowest = None

    def get_min(seed):
        min_stop = float("inf")
        current = seed

        for m in maps:
            sub_map = next((s for s in m if s[1] <= current <= s[1] + s[2]), None)

            if sub_map is None:
                continue

            dest, source, rng = sub_map

            stop = rng - (current - source)

            if stop < min_stop:
                min_stop = stop

            position = current - source
            current = dest + position

        return min_stop

    # The sequence is linear for a certain range
    for i in range(0, len(seeds), 2):
        start = seeds[i]
        end = seeds[i] + seeds[i + 1]

        while start < end:
            temp = convert_seed(start)

            if lowest is None or temp < lowest:
                lowest = temp

            increment = get_min(start)

            if increment == 0:
                increment = 1

            start += increment

    return lowest


submit(part=1, day=5, year=2023, answer=solve1())
submit(part=2, day=5, year=2023, answer=solve2())
