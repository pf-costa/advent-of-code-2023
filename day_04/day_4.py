from aocd import submit, get_data

data = get_data(day=4, year=2023).split("\n")
cards = []
numbers = []


def extract_numbers(part):
    return [int(number) for number in part.strip().split(" ") if number.isdigit()]


for line in data:
    [part1, part2] = line.split(":")
    [part1, part2] = part2.split("|")

    cards.append(extract_numbers(part1))
    numbers.append(extract_numbers(part2))


def count_winning_numbers(card_index):
    return sum(1 for element in cards[card_index] if element in numbers[card_index])


def solve1():
    total = 0

    for i, _ in enumerate(cards):
        count = count_winning_numbers(i)

        if count > 0:
            total += 2 ** (count - 1)

    return total


def solve2():
    instances = [1] * len(cards)

    for i, _ in enumerate(cards):
        count = count_winning_numbers(i)
        current_instances = instances[i]

        for card in range(1, count + 1):
            instances[i + card] += current_instances

    return sum(instances)


submit(part=1, day=4, year=2023, answer=solve1())
submit(part=2, day=4, year=2023, answer=solve2())
