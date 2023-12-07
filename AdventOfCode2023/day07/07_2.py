import sys
from collections import Counter

named_card_to_number = {'T': 10, 'J': 1, 'Q': 11, 'K': 12, 'A': 13}


def read_input() -> list[str]:
    return [line.strip() for line in sys.stdin]


def evaluate_hand(hand: str) -> tuple[int, tuple[int]]:
    hand_counter = Counter(hand)

    # {5} => Five of a kind     => 7
    # {4, 1} => Four of a kind  => 6
    # {3, 2} => Full house      => 5
    # {3, 1} => Three of a kind => 4
    # {2, 1} => Two pair        => 3
    # {2, 1} => One pair        => 2
    # {1} => High card          => 1

    counts = set(hand_counter.values())

    if counts == set([5]):
        hand_type = 7
    elif counts == set([1, 4]):
        hand_type = 6

        # We can have 0, 1 or 4 Js
        if hand_counter['J'] == 1 or hand_counter['J'] == 4:
            hand_type = 7

    elif counts == set([2, 3]):
        hand_type = 5

        # We can have 0, 2 or 3 Js
        if hand_counter['J'] == 2 or hand_counter['J'] == 3:
            hand_type = 7

    elif counts == set([1, 3]):
        hand_type = 4

        # We can have 0, 1 or 3 Js
        if hand_counter['J'] == 3 or hand_counter['J'] == 1:
            hand_type = 6

    elif counts == set([1, 2]) and list(hand_counter.values()).count(2) == 2:
        # Two pairs
        hand_type = 3

        # We can have 0, 1 or 2Js

        if hand_counter['J'] == 1:
            hand_type = 5
        elif hand_counter['J'] == 2:
            hand_type = 6

    elif counts == set([1, 2]) and list(hand_counter.values()).count(2) != 2:
        # One pair
        hand_type = 2

        # We can have 0, 1 or 2Js
        if hand_counter['J'] == 1 or hand_counter['J'] == 2:
            hand_type = 4

    elif counts == set([1]):
        hand_type = 1

        if hand_counter['J'] == 1:
            hand_type = 2
    else:
        hand_type = -1

    hand_strength = tuple(int(card) if card.isnumeric() else named_card_to_number[card]
                          for card in hand)

    return hand_type, hand_strength


if __name__ == "__main__":
    lines = read_input()

    lines = [line.split() for line in lines]

    lines = sorted(lines, key=lambda x: evaluate_hand(x[0]))

    winnings = [int(bid) * rank for rank, (_, bid) in enumerate(lines, start=1)]

    result = sum(winnings)

    print(result)
