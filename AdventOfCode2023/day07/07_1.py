import sys
from collections import Counter

named_card_to_number = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}


def read_input() -> list[str]:
    return [line.strip() for line in sys.stdin]


def evaluate_hand(hand: str) -> tuple[int, tuple[int]]:
    hand_counter = Counter(hand)

    # {5} => Five of a kind
    # {4, 1} => Four of a kind
    # {3, 2} => Full house
    # {3, 1} => Three of a kind
    # {2, 1} => Two pair
    # {2, 1} => One pair
    # {1} => High card

    counts = set(hand_counter.values())

    if counts == set([5]):
        hand_type = 7
    elif counts == set([1, 4]):
        hand_type = 6
    elif counts == set([2, 3]):
        hand_type = 5
    elif counts == set([1, 3]):
        hand_type = 4
    elif counts == set([1, 2]) and list(hand_counter.values()).count(2) == 2:
        hand_type = 3
    elif counts == set([1, 2]) and list(hand_counter.values()).count(2) != 2:
        hand_type = 2
    elif counts == set([1]):
        hand_type = 1
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
