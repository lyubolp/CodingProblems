import time
import sys
from collections import namedtuple

Point = namedtuple('Point', ['i', 'j'])
offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def read_input() -> list[str]:
    return [line.strip() for line in sys.stdin]


def find_galaxies(line: str, current_row: int) -> list[Point]:
    return [Point(current_row, j) for j, c in enumerate(line) if c == '#']


def expand_galaxies(galaxies: list[Point], empty_rows: list[int], empty_cols: list[int]) -> list[Point]:
    expanded_galaxies = [expand_galaxy(galaxy, empty_rows, empty_cols) for galaxy in galaxies]
    return expanded_galaxies


def expand_galaxy(galaxy: Point, empty_rows: list[int], empty_cols: list[int]) -> Point:
    offset_i = sum(999_999 for i, row in enumerate(empty_rows, start=1) if row < galaxy.i)
    offset_j = sum(999_999 for j, col in enumerate(empty_cols, start=1) if col < galaxy.j)

    return Point(galaxy.i + offset_i, galaxy.j + offset_j)


def distance_between_two_galaxies(start: Point, end: Point, bounds: Point) -> dict[Point, int]:
    return abs(start.i - end.i) + abs(start.j - end.j)


def is_point_inside(point: Point, bounds: Point) -> bool:
    return 0 <= point.i < bounds.i and 0 <= point.j < bounds.j


if __name__ == "__main__":
    lines = read_input()

    galaxies = sum([find_galaxies(line, i) for i, line in enumerate(lines)], [])

    empty_rows = [i for i, row in enumerate(lines) if '#' not in row]
    empty_cols = [j for j, col in enumerate(zip(*lines)) if '#' not in col]

    galaxies = expand_galaxies(galaxies, empty_rows, empty_cols)

    bounds = Point(len(lines) + len(empty_rows) + 1, len(lines[0]) + len(empty_rows) + 1)

    galaxy_pairs = [(galaxy_i, galaxy_j)
                    for i, galaxy_i in enumerate(galaxies)
                    for j, galaxy_j in enumerate(galaxies)
                    if j > i]

    distances = [distance_between_two_galaxies(galaxy_i, galaxy_j, bounds)
                 for galaxy_i, galaxy_j in galaxy_pairs]

    result = sum(distances)
    print(result)
