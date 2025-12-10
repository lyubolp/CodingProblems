import sys

from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])


def read_input() -> list[str]:
    return [line.strip() for line in sys.stdin]


def parse_input(lines: list[str]) -> list[Point]:
    return [parse_line(line) for line in lines]


def parse_line(line: str) -> Point:
    x, y = line.split(",")

    return Point(int(x), int(y))


def calculate_area(first: Point, second: Point) -> int:
    width = abs(first.x - second.x + 1)
    height = abs(first.y - second.y + 1)

    return width * height


def generate_all_rectangles(tiles: list[Point]) -> list[list[Point]]:
    return [[first, second] for i, first in enumerate(tiles) for second in tiles[i + 1 :]]


if __name__ == "__main__":
    lines = read_input()

    tiles = parse_input(lines)

    pairs = generate_all_rectangles(tiles)

    # for first, second in pairs:
    #     print(f"{first}, {second} - {calculate_area(first, second)}")

    result = max(calculate_area(first, second) for first, second in pairs)
    print(result)
