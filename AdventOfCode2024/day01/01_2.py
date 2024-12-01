import sys

from collections import Counter


def read_input() -> list[str]:
    return [line.strip() for line in sys.stdin]


if __name__ == "__main__":
    lines = read_input()

    pairs = [line.split() for line in lines]
    pairs = [(int(pair[0]), int(pair[1])) for pair in pairs]

    left = [pair[0] for pair in pairs]
    right = [pair[1] for pair in pairs]

    right_count = Counter(right)

    similarity_score = [number * right_count.get(number, 0) for number in left]

    print(sum(similarity_score))
