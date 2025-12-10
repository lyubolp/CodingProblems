import sys


def read_input() -> list[str]:
    return [line.strip() for line in sys.stdin]


if __name__ == "__main__":
    lines = read_input()
    print(lines)
