#!/usr/bin/python3
import re
import sys
from collections import namedtuple
from typing import List, Tuple, Dict, Set
from queue import PriorityQueue

Point = namedtuple('Point', ['x', 'y'])
Probe = namedtuple('Probe', ['x', 'y', 'x_velocity', 'y_velocity'])


def read_input() -> List[str]:
    return [line.strip() for line in sys.stdin if line != '\n']


def get_coordinates(line: str) -> List[Point]:
    # Regex magic - finds the coordinates
    p = re.compile(".*x=(-?[0-9]*)..(-?[0-9]*).*y=(-?[0-9]*)..(-?[0-9]*).*")

    groups = p.search(line).groups()
    if len(groups) != 4:
        raise ValueError("Unable to parse")

    start = Point(int(groups[0]), int(groups[2]))
    end = Point(int(groups[1]), int(groups[3]))

    return [start, end]


def is_probe_inside_rectangle(probe: Probe, top_left: Point, bottom_right: Point) -> bool:
    return top_left.x <= probe.x <= bottom_right.x and top_left.y <= probe.y <= bottom_right.y


def step(probe: Probe) -> Probe:
    new_x_velocity = probe.x_velocity

    if probe.x_velocity > 0:
        new_x_velocity -= 1
    elif probe.x_velocity < 0:
        new_x_velocity += 1
    else:
        new_x_velocity = 0

    return Probe(probe.x + probe.x_velocity, probe.y + probe.y_velocity,
                 new_x_velocity, probe.y_velocity - 1)


def is_probe_passed_rectangle(probe: Probe, top_left: Point, bottom_right: Point) -> bool:
    is_after_x = bottom_right.x < probe.x
    is_after_y = probe.y < top_left.y

    return is_after_x or is_after_y


if __name__ == "__main__":
    line = read_input()[0]
    start, end = get_coordinates(line)

    results = []
    x_velocity_range = max([abs(start.x), abs(end.x)])
    y_velocity_range = max([abs(start.y), abs(end.y)])

    print(start, end)
    for x_velocity in range(x_velocity_range + 1):
        for y_velocity in range(-y_velocity_range - 1, y_velocity_range + 1):
            probe = Probe(0, 0, x_velocity, y_velocity)
            initial_x_velocity, initial_y_velocity = x_velocity, y_velocity

            while not is_probe_passed_rectangle(probe, start,
                                                end) and not is_probe_inside_rectangle(probe, start,
                                                                                       end):
                probe = step(probe)

            if is_probe_inside_rectangle(probe, start, end):
                results.append((initial_x_velocity, initial_y_velocity))

    print(len(results))
