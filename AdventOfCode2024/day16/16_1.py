import itertools
import math
import heapq
import sys
from collections import namedtuple

Point = namedtuple("Point", ["i", "j"])

direction_to_point = {"E": Point(0, 1), "W": Point(0, -1), "N": Point(-1, 0), "S": Point(1, 0)}
clockwise = {"E": "S", "S": "W", "W": "N", "N": "E"}
counter_clockwise = {"E": "N", "N": "W", "W": "S", "S": "E"}


def read_input() -> list[str]:
    return [line.strip() for line in sys.stdin]


def djikstra(start: Point, target: Point, bounds: Point, walls: set[Point]) -> int:
    unvisited = []
    visited = set()

    heapq.heappush(unvisited, (0, start, "E"))

    for i in range(bounds.i):
        for j in range(bounds.j):
            heapq.heappush(unvisited, (math.inf, Point(i, j), "E"))

    while len(unvisited) > 0:
        current_distance, current_node, current_direction = heapq.heappop(unvisited)

        if (current_node, current_direction) in visited:
            continue

        if current_node in walls:
            continue

        if current_node == target:
            return current_distance

        neighbours = [
            (
                current_distance + 1,
                add(current_node, direction_to_point[current_direction]),
                current_direction,
            ),
            (
                current_distance + 1000,
                current_node,
                clockwise[current_direction],
            ),
            (
                current_distance + 1000,
                current_node,
                counter_clockwise[current_direction],
            ),
        ]

        for neighbour in neighbours:
            heapq.heappush(unvisited, neighbour)

        visited.add((current_node, current_direction))

    return -1


def add(first: Point, second: Point) -> Point:
    return Point(first.i + second.i, first.j + second.j)


if __name__ == "__main__":
    lines = read_input()

    walls = set()
    for i, row in enumerate(lines):
        for j, content in enumerate(row):
            if content == "S":
                start = Point(i, j)
            elif content == "E":
                target = Point(i, j)
            elif content == "#":
                walls.add(Point(i, j))

    bounds = Point(len(lines), len(lines[0]))
    print(djikstra(start, target, bounds, walls))
