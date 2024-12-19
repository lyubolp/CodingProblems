import sys

from collections import namedtuple

Point = namedtuple('Point', ['i', 'j'])
offsets = [Point(0, 1), Point(0, -1), Point(1, 0), Point(-1, 0)]


def read_input() -> list[str]:
    return [line.strip() for line in sys.stdin]


def parse_line(line: str) -> Point:
    i, j = line.split(',')

    return Point(int(j), int(i))


def parse_lines(lines: list[str], amount: int) -> set[Point]:
    return {parse_line(line) for line in lines[:amount]}


def bfs(start: Point, target: Point, bounds: Point, blocked: set[Point]) -> int:
    queue = [(start, 0)]

    visited = set()
    while len(queue) > 0:
        current_point, current_distance = queue.pop(0)

        if current_point == target:
            return current_distance

        if current_point in visited:
            continue

        if not is_point_within_bounds(current_point, bounds):
            continue
        
        # print(current_point)
        for offset in offsets:
            next_point = add(current_point, offset)

            if next_point not in blocked:
                queue.append((next_point, current_distance + 1))

        visited.add(current_point)
    
    return -1


def is_point_within_bounds(point: Point, bounds: Point) -> bool:
    return 0 <= point.i < bounds.i and 0 <= point.j < bounds.j


def add(first: Point, second: Point) -> Point:
    return Point(first.i + second.i, first.j + second.j)


def print_grid(bounds: Point, blocked: set[Point]):
    for i in range(bounds.i):
        for j in range(bounds.j):
            if Point(i, j) in blocked:
                print('#', end="")
            else:
                print(".", end="")
        print("")


if __name__ == "__main__":
    lines = read_input()

    left = 0
    right = len(lines) - 1
    mid = (right - left) // 2

    while right - left > 0:
        mid =  ((right - left) // 2) + left
        blocked = parse_lines(lines, mid)

        bounds = Point(71, 71)
        target = Point(70, 70)

        result = bfs(Point(0, 0), target, bounds, blocked)

        if result == -1:
            right = mid
        else:
            left = mid + 1

    print(lines[mid])
