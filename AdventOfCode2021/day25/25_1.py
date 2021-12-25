#!/usr/bin/python3
import copy
import math
import sys

from collections import namedtuple
from functools import reduce
from typing import List, Tuple, Dict

Point = namedtuple('Point', ['i', 'j'])


def generate_next_point(current: Point, is_east: bool, max_i: int, max_j: int) -> Point:
    if is_east:
        return Point(current.i, current.j + 1 if current.j < max_j - 1 else 0)
    else:
        return Point(current.i + 1 if current.i < max_i - 1 else 0, current.j)


def read_input() -> List[str]:
    return [line.strip() for line in sys.stdin if line != '\n']


def parse_char(char: str) -> int:
    if char == '.':
        return 0
    elif char == '>':
        return 1
    elif char == 'v':
        return 2


def parse_line(line: str) -> List[int]:
    return [parse_char(c) for c in line]


def parse_input(lines: List[str]) -> Dict[Point, str]:
    result = {}
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == 'v' or c == '>':
                result[Point(i, j)] = c

    return result


def move(matrix: Dict[Point, str], max_i: int, max_j: int, direction: str) -> Dict[Point, str]:
    result = {}
    for point in matrix:
        if matrix[point] == direction:
            new_location = generate_next_point(point, direction == '>', max_i, max_j)

            if new_location not in matrix:
                result[new_location] = matrix[point]
            else:
                result[point] = matrix[point]
        else:
            result[point] = matrix[point]

    return result


def step(matrix: Dict[Point, str], max_i: int, max_j: int) -> int:
    prev = {}
    steps = 0
    while prev != matrix:
        prev = matrix
        matrix = move(matrix, max_i, max_j, '>')
        matrix = move(matrix, max_i, max_j, 'v')
        steps += 1

        # print(f"After {steps} step")
        # visualize(matrix, max_i, max_j)
    return steps


def visualize(matrix: Dict[Point, str], max_i: int, max_j: int):
    result = [['.' for j in range(max_j)] for i in range(max_i)]

    for point in matrix:
        result[point.i][point.j] = matrix[point]

    for row in result:
        print("".join(row))


if __name__ == "__main__":
    lines = read_input()
    max_i = len(lines)
    max_j = len(lines[0])
    matrix = parse_input(lines)

    # visualize(matrix, max_i, max_j)
    print(step(matrix, max_i, max_j))
