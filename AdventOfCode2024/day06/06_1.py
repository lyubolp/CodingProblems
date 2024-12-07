import sys

from collections import namedtuple

Point = namedtuple("Point", ["i", "j"])
directions = [Point(-1, 0), Point(0, 1), Point(1, 0), Point(0, -1)]


def read_input() -> list[str]:
    return [line.strip() for line in sys.stdin]


def is_point_within_bounds(point: Point, bounds: Point) -> bool:
    return 0 <= point.i < bounds.i and 0 <= point.j < bounds.j


def offset_point(first: Point, second: Point) -> Point:
    return Point(first.i + second.i, first.j + second.j)


def walk_around(guard: Point, obstacles: set[Point], bounds: Point) -> int:
    visited = set()

    current_direction = 0

    next_move = offset_point(guard, directions[current_direction])

    while is_point_within_bounds(guard, bounds):
        visited.add(guard)
        if next_move not in obstacles:
            guard = next_move
        else:
            current_direction = (current_direction + 1) % 4
        next_move = offset_point(guard, directions[current_direction])

    return len(visited)


if __name__ == "__main__":
    lines = read_input()

    bounds = Point(len(lines), len(lines[0]))

    obstacles = set()
    for i, line in enumerate(lines):
        for j, content in enumerate(line):
            if content == "#":
                obstacles.add(Point(i, j))
            if content == "^":
                guard = Point(i, j)

    print(walk_around(guard, obstacles, bounds))
