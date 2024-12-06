import sys
from collections import namedtuple
from functools import reduce

Point = namedtuple('Point', ['i', 'j'])
XMAS = 'XMAS'
offsets = [Point(1, 0), Point(-1, 0), Point(0, 1), Point(0, -1), Point(-1, 1), Point(1, -1), Point(1, 1), Point(-1, -1)]

def read_input() -> list[str]:
    return [line.strip() for line in sys.stdin]

def build_matrix(lines: list[str]) -> dict[Point, str]:
    return {Point(i, j): content for i, row in enumerate(lines) for j, content in enumerate(row)}

def is_containing_xmas(matrix: dict[Point, str], start: Point, bounds: Point) -> int:
    return sum(1 for offset in offsets if is_containing_xmas_in_direction(start, matrix, offset, bounds))

def is_containing_xmas_in_direction(start: Point, matrix: dict[Point, str], direction: Point, bounds: Point) -> bool:
    result = []
    current = start

    for _ in XMAS:
        if not is_point_within_bounds(current, bounds):
            continue
        result.append(matrix[current])
        current = offset_point(current, direction)

    return ''.join(result) == XMAS

def is_point_within_bounds(point: Point, bounds: Point) -> bool:
    return 0 <= point.i < bounds.i and 0 <= point.j < bounds.j

def offset_point(first: Point, second: Point) -> Point:
    return Point(first.i + second.i, first.j + second.j)

if __name__ == "__main__":
    lines = read_input()

    bounds = Point(len(lines), len(lines[0]))
    matrix = build_matrix(lines)

    result = sum(is_containing_xmas(matrix, point, bounds) for point, letter in matrix.items() if letter == 'X')
    print(result)

