#!/usr/bin/python3

import sys
import re

from collections import namedtuple
from typing import List, Tuple

Point = namedtuple('Point', ['x', 'y', 'z'])
Step = namedtuple('Step', ['is_on', 'start_x', 'end_x', 'start_y', 'end_y', 'start_z', 'end_z'])


def read_input() -> List[str]:
    return [line.strip() for line in sys.stdin if line != '\n']


def handle_line(line: str) -> Step:
    on_off = line.split(' ')[0]
    is_on_off = True if on_off == 'on' else False

    coordinates = line.split(' ')[1].split(',')

    coordinates_re = re.compile("=(-?[0-9]*)..(-?[0-9]*)")

    parsed_coordinates = [coordinates_re.search(coord).groups() for coord in coordinates]

    return Step(is_on_off,
                int(parsed_coordinates[0][0]), int(parsed_coordinates[0][1]),
                int(parsed_coordinates[1][0]), int(parsed_coordinates[1][1]),
                int(parsed_coordinates[2][0]), int(parsed_coordinates[2][1]))


def build_range(step: Step) -> List[Point]:
    result = []

    if step.start_x < -50 or step.start_y < -50 or step.start_z < -50 or step.end_x > 50 or step.end_y > 50 or step.end_z > 50:
        return []

    for x in range(step.start_x, step.end_x + 1):
        for y in range(step.start_y, step.end_y + 1):
            for z in range(step.start_z, step.end_z + 1):
                result.append(Point(x, y, z))

    return result


if __name__ == "__main__":
    lines = read_input()
    inputs = [handle_line(line) for line in lines]

    result = {}

    for input in inputs:
        for point in build_range(input):
            result[point] = input.is_on

    print(len([point for point in result if result[point]]))
