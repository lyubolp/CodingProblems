import sys
from collections import defaultdict, namedtuple
from itertools import product

Point = namedtuple("Point", ["i", "j"])


def read_input() -> list[str]:
    return [line.strip() for line in sys.stdin]


def parse_antenas(lines: list[str]) -> dict[str, set[Point]]:
    antenas = defaultdict(set)

    for i, row in enumerate(lines):
        for j, content in enumerate(row):
            if content != '.':
                antenas[content].add(Point(i, j))

    return antenas


def add(first: Point, second: Point) -> Point:
    return Point(first.i + second.i, first.j + second.j)


def subtract(first: Point, second: Point) -> Point:
    return Point(first.i - second.i, first.j - second.j)


def invert_point(point: Point) -> Point:
    return Point(-point.i, -point.j)


def le_than(first: Point, second: Point) -> bool:
    return first.i <= second.i and first.j <= second.j


def is_point_within_bounds(point: Point, bounds: Point) -> bool:
    return 0 <= point.i < bounds.i and 0 <= point.j < bounds.j


def calculate_antinodes(first: Point, second: Point, bounds: Point) -> set[Point]:
    result = set()

    diff = subtract(first, second)
    # OG direction
    current = first

    while is_point_within_bounds(current, bounds):
        result.add(current)
        current = add(current, diff)

    # Other direction
    diff = invert_point(diff)

    current = first

    while is_point_within_bounds(current, bounds):
        result.add(current)
        current = add(current, diff)

    return result


if __name__ == "__main__":
    lines = read_input()
    all_antenas = parse_antenas(lines)
    # print(sorted(all_antenas['#']))

    bounds = Point(len(lines), len(lines[0]))

    antinodes = set()

    for antenas in all_antenas.values():
        for first, second in product(antenas, antenas):
            if first != second:
                antinodes |= calculate_antinodes(first, second, bounds)

    antinodes = set(point for point in antinodes if is_point_within_bounds(point, bounds))
    # print(sorted(antinodes))
    print(len(antinodes))