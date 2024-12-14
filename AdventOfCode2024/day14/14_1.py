import sys
from collections import namedtuple
from functools import reduce

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


def move_robot(robot: Point, velocity: Point, seconds: int, bounds: Point) -> Point:
    new_x = (robot.x + (seconds * velocity.x)) % bounds.x
    new_y = (robot.y + (seconds * velocity.y)) % bounds.y

    return Point(new_x, new_y)


def count_robots_in_quadrant(robots: list[tuple[Point, Point]], bounds: Point, quadrant: int, quadrant_x: int, quadrant_y: int) -> int:
    if quadrant == 1 or quadrant == 2:
        start_x, end_x = 0, quadrant_x
    else:
        start_x, end_x = bounds.x - quadrant_x, bounds.x

    if quadrant == 1 or quadrant == 3:
        start_y, end_y = 0, quadrant_y
    else:
        start_y, end_y = bounds.y - quadrant_y, bounds.y

    return sum(1 for robot, _ in robots if start_x <= robot.x < end_x and start_y <= robot.y < end_y)


if __name__ == "__main__":
    lines = read_input()

    robots = [parse_line(line) for line in lines]
    bounds = Point(7, 11)
    bounds = Point(103, 101)

    seconds = 100
    robots = [(move_robot(robot, velocity, seconds, bounds), velocity) for robot, velocity in robots]

    quadrant_x = bounds.x // 2
    quadrant_y = bounds.y // 2

    robots_in_quadrants = [count_robots_in_quadrant(robots, bounds, quadrant, quadrant_x, quadrant_y) for quadrant in range(1, 5)]

    print(reduce(lambda x, y: x * y, robots_in_quadrants, 1))
