import sys
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])


def read_input() -> list[str]:
    return [line.strip() for line in sys.stdin]


def parse_line(line: str) -> tuple[Point, Point]:
    position, velocity = line.split()

    position = position.split("=")[1].split(",")
    velocity = velocity.split("=")[1].split(",")

    return Point(int(position[1]), int(position[0])), Point(int(velocity[1]), int(velocity[0]))


def draw_grid(bounds: Point, robots):
    for i in range(bounds.x):
        for j in range(bounds.y):
            robots_in_place = sum(1 for robot, _ in robots if robot == Point(i, j))
            if robots_in_place > 0:
                print(str(robots_in_place), end="")
            else:
                print(".", end="")
        print("")


if __name__ == "__main__":
    lines = read_input()

    robots = [parse_line(line) for line in lines]

    bounds = Point(7, 11)
    draw_grid(bounds, robots)
