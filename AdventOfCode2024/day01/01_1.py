import sys


def read_input() -> list[str]:
    return [line.strip() for line in sys.stdin]


if __name__ == "__main__":
    lines = read_input()

    pairs = [line.split() for line in lines]
    pairs = [(int(pair[0]), int(pair[1])) for pair in pairs]

    left = sorted([pair[0] for pair in pairs])
    right = sorted([pair[1] for pair in pairs])

    diffs = [abs(a - b) for a, b in zip(left, right)]

    print(sum(diffs))
