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


def print_tiles(red: list[Point], green: list[Point], bounds: Point):
    red_tiles = set(red)
    green_tiles = set(green)

    for i in range(bounds.x):
        for j in range(bounds.y):
            if Point(i, j) in red_tiles:
                print("#", end="")
            elif Point(i, j) in green_tiles:
                print("X", end="")
            else:
                print(".", end="")
        print("")


if __name__ == "__main__":
    lines = read_input()

    tiles = parse_input(lines)

    max_point = max(tiles)
    bounds = Point(max_point.x + 2, max_point.y + 2)

    pairs = generate_all_rectangles(tiles)

    print_tiles(tiles, [], bounds)

    # for first, second in pairs:
    #     print(f"{first}, {second} - {calculate_area(first, second)}")

    # result = max(calculate_area(first, second) for first, second in pairs)
    # print(result)
