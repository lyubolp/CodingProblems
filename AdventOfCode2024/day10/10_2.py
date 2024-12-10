import sys
from collections import namedtuple

Point = namedtuple("Point", ["i", "j"])
offsets = [Point(0, 1), Point(0, -1), Point(1, 0), Point(-1, 0)]


def read_input() -> list[str]:
    return [line.strip() for line in sys.stdin]


def parse_map(lines: list[str]) -> dict[Point, int]:
    return {Point(i, j): int(height) for i, row in enumerate(lines) for j, height in enumerate(row)}


def dfs(start: Point, height_map: dict[Point, int], bounds: Point) -> int:
    result = set()

    stack = [(start, set())]

    while len(stack) > 0:
        current_point, current_visited = stack.pop()

        if current_point in current_visited:
            continue

        if height_map[current_point] == 9:
            result.add(frozenset(current_visited | {current_point}))

        all_neighbours = [add(current_point, offset) for offset in offsets]
        neighbours_within_bounds = [point for point in all_neighbours if is_point_within_bounds(point, bounds)]
        neighbours_increasing = [point for point in neighbours_within_bounds if height_map[point] == height_map[current_point] + 1]

        neighbours = [(point, current_visited | {current_point}) for point in neighbours_increasing]

        stack += neighbours

    return len(result)


def is_point_within_bounds(point: Point, bounds: Point) -> bool:
    return 0 <= point.i < bounds.i and 0 <= point.j < bounds.j


def add(first: Point, second: Point) -> Point:
    return Point(first.i + second.i, first.j + second.j)


if __name__ == "__main__":
    lines = read_input()

    height_map = parse_map(lines)
    bounds = Point(len(lines), len(lines[0]))

    results = [dfs(point, height_map, bounds) for point, height in height_map.items() if height == 0]

    print(sum(results))

