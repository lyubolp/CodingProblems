import sys
from collections import namedtuple

Point = namedtuple("Point", ["i", "j"])

moves = {"^": Point(-1, 0), ">": Point(0, 1), "<": Point(0, -1), "v": Point(1, 0)}


def read_input() -> list[str]:
    return [line.strip() for line in sys.stdin]


def parse_robot_map(lines: list[str]) -> dict[Point, str]:
    return {
        Point(i, j): content
        for i, row in enumerate(lines)
        for j, content in enumerate(row)
        if content != "."
    }


def parse_robot_moves(lines: list[str]) -> list[Point]:
    return [moves[move] for move in "".join(lines)]


def move_robot(
    current: Point, robot_map: dict[Point, str], next_move: Point
) -> tuple[Point, dict[Point, str]]:
    next_position = add(current, next_move)

    if next_position not in robot_map:
        return next_position, robot_map

    if robot_map[next_position] == "#":
        return current, robot_map

    if robot_map[next_position] == "O":
        new_robot = Point(next_position.i, next_position.j)

        last_box = next_position
        while add(last_box, next_move) in robot_map and robot_map[add(last_box, next_move)] == "O":
            last_box = add(last_box, next_move)

        after_last_box = add(last_box, next_move)
        if after_last_box not in robot_map:
            robot_map[after_last_box] = "O"
            del robot_map[new_robot]
            return new_robot, robot_map

    return current, robot_map


def add(first: Point, second: Point) -> Point:
    return Point(first.i + second.i, first.j + second.j)


def inverse(point: Point) -> Point:
    return Point(-point.i, -point.j)


def draw_grid(robot_position, robot_map):
    bounds = max(robot_map)

    for i in range(bounds.i + 1):
        for j in range(bounds.j + 1):
            if Point(i, j) == robot_position:
                print("@", end="")
            elif Point(i, j) not in robot_map:
                print(".", end="")
            else:
                print(robot_map[Point(i, j)], end="")
        print("")
    print("")


if __name__ == "__main__":
    lines = read_input()
    for i, line in enumerate(lines):
        if line == "":
            robot_map = parse_robot_map(lines[:i])
            robot_moves = parse_robot_moves(lines[i + 1 :])
            break

    robot_position = next(position for position, content in robot_map.items() if content == "@")
    del robot_map[robot_position]

    # draw_grid(robot_position, robot_map)

    for robot_move in robot_moves:
        robot_position, robot_map = move_robot(robot_position, robot_map, robot_move)
        # draw_grid(robot_position, robot_map)

    print(
        sum(
            100 * position.i + position.j
            for position, content in robot_map.items()
            if content == "O"
        )
    )
