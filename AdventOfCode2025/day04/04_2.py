import sys

from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
offsets = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]


def read_input() -> list[str]:
    return [line.strip() for line in sys.stdin]


def parse_lines(lines: list[str]) -> set[Point]:
    return set(Point(x, y) for x, row in enumerate(lines) for y, item in enumerate(row) if item == "@")


def get_neighbors(start: Point, rolls: set[Point]) -> set[Point]:
    return set(
        new_point
        for offset_x, offset_y in offsets
        if (new_point := Point(start.x + offset_x, start.y + offset_y)) in rolls
    )


if __name__ == "__main__":
    lines = read_input()
    m, n = len(lines), len(lines[0])
    rolls = parse_lines(lines)

    accessible_rolls = set(roll for roll in rolls if len(get_neighbors(roll, rolls)) < 4)

    result = 0
    while len(accessible_rolls) > 0:
        rolls = rolls - accessible_rolls
        result += len(accessible_rolls)
        accessible_rolls = set(roll for roll in rolls if len(get_neighbors(roll, rolls)) < 4)

    print(result)
    # for i in range(m):
    #     for j in range(n):
    #         candidate = Point(i, j)
    #         if Point(i, j) in rolls:
    #             if len(get_neighbors(candidate, rolls)) < 4:
    #                 print("x", end="")
    #             else:
    #                 print("@", end="")
    #         else:
    #             print(".", end="")
    #     print("")
