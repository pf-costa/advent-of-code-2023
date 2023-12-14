from functools import reduce
from aocd import submit, get_data
import operator
import math
from collections import defaultdict
from functools import cmp_to_key

data = get_data(day=7, year=2023)

JOKER = "J"

type_card = ["A", "K", "Q", JOKER, "T", "9", "8", "7", "6", "5", "4", "3", "2"]
type_card.reverse()

plays = [(hand, int(bid)) for line in data.split("\n") for hand, bid in [line.split()]]


def evaluate_poker_hand(hand):
    # Count the occurrences of each card type in the hand
    card_counts = {card: hand.count(card) for card in type_card if hand.count(card) > 0}

    card_type = 0

    # Check for specific poker hands using if-else statements
    if 5 in card_counts.values():
        card_type = 7  # Five of a Kind
    elif 4 in card_counts.values():
        card_type = 6  # Four of a Kind
    elif set(card_counts.values()) == {3, 2}:
        card_type = 5  # Full House
    elif 3 in card_counts.values():
        card_type = 4  # Three of a Kind
    elif list(card_counts.values()).count(2) == 2:
        card_type = 3  # Two Pair
    elif 2 in card_counts.values():
        card_type = 2  # One Pair
    else:
        card_type = 1

    return card_type


def get_play_value(item):
    index, (_, bid, _) = item
    r = bid * (index + 1)
    return r


def get_card_value(card):
    return len(type_card) - type_card.index(card) - 1


def compare_cards(x, y):
    if x[0] != y[0]:
        return x[0] - y[0]

    for i in range(0, len(x[2])):
        if x[2][i] == y[2][i]:
            continue

        return get_card_value(y[2][i]) - get_card_value(x[2][i])

    return 0


def solve1():
    bids = []

    for hand, bid in plays:
        value = evaluate_poker_hand(hand)
        bids.append((value, bid, hand))

    # Sort the list by value and then by applying the custom sorting for "hand"
    sorted_bids = sorted(bids, key=cmp_to_key(compare_cards))

    return sum(
        map(
            get_play_value,
            enumerate(sorted_bids),
        )
    )


def solve2():
    # I shouldn't mutating the main array, but I'm lazy
    type_card.remove(JOKER)
    type_card.insert(0, JOKER)

    bids = []

    def apply_joker_rule(hand):
        if JOKER not in hand:
            return hand

        card_counts = {
            card: hand.count(card)
            for card in type_card
            if hand.count(card) > 0 and card != JOKER
        }

        if not any(card_counts):
            card = "A"
        else:
            [card, _] = max(card_counts.items(), key=lambda x: x[1])

        return hand.replace(JOKER, card)

    for hand, bid in plays:
        new_hand = apply_joker_rule(hand)
        value = evaluate_poker_hand(new_hand)
        bids.append((value, bid, hand))

    # Sort the list by value and then by applying the custom sorting for "hand"
    sorted_bids = sorted(bids, key=cmp_to_key(compare_cards))

    return sum(
        map(
            get_play_value,
            enumerate(sorted_bids),
        )
    )


submit(part=1, day=7, year=2023, answer=solve1())
submit(part=2, day=7, year=2023, answer=solve2())
