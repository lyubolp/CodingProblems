import sys

from collections import namedtuple
from enum import Enum
from typing import Dict, List, Tuple, Callable, Union, Optional, Set

Point = namedtuple('Point', ['x', 'y'])

def read_input() -> List[str]:
    return [line for line in sys.stdin]

def parse_char(char: str, x: int, y: int) -> Point:
    if char == '#':
        return Point(x + 1, y + 1), '#'
    return Point(x + 1, y + 1), '.'

def parse_input(input: str, y: int) -> List[Point]:
    return [parse_char(char, x, y) for x, char in enumerate(input[:-1]) if char != ' ']

def parse_movements(movements: str) -> List[Union[int, str]]:
    movements = ' L '.join(movements.split('L'))
    movements = ' R '.join(movements.split('R'))

    return [c if c.isalpha() else int(c) for c in movements.split(' ')]

def rotate(direction: str, rotation: str) -> str:
    if direction == 'R':
        if rotation == 'R':
            return 'D'
        else:
            return 'U'
    elif direction == 'L':
        if rotation == 'R':
            return 'U'
        else:
            return 'D'
    elif direction == 'U':
        if rotation == 'R':
            return 'R'
        else:
            return 'L'
    elif direction == 'D':
        if rotation == 'R':
            return 'L'
        else:
            return 'R'


def get_next_position(position: Point, direction: str) -> Point:
    if direction == 'R':
        return Point(position.x + 1, position.y)
    elif direction == 'L':
        return Point(position.x - 1, position.y)
    elif direction == 'U':
        return Point(position.x, position.y - 1)
    elif direction == 'D':
        return Point(position.x, position.y + 1)


def wrap_around(position: Point, direction: str, field: Dict[Point, str]) -> Point:
    if direction == 'R':
        on_current_row = [point for point in field if point.y == position.y]
        on_current_row.sort(key=lambda point: point.x)
        return on_current_row[0]
    elif direction == 'L':
        on_current_row = [point for point in field if point.y == position.y]
        on_current_row.sort(key=lambda point: point.x)
        return on_current_row[-1]
    elif direction == 'U':
        on_current_column = [point for point in field if point.x == position.x]
        on_current_column.sort(key=lambda point: point.y)
        return on_current_column[-1]
    elif direction == 'D':
        on_current_column = [point for point in field if point.x == position.x]
        on_current_column.sort(key=lambda point: point.y)
        return on_current_column[0]


def move(position: Point, direction: str, field: Dict[Point, str]) -> Point:
    next_position = get_next_position(position, direction)
    
    if next_position not in field:
        next_position = wrap_around(position, direction, field)

    if field[next_position] == '#':
        return position

    return next_position

def moves(movements: List[Union[int, str]], current: Tuple[Point, str], field: List[List[Point]]) -> Tuple[Point, str]:
    position, direction = current
    for movement in movements:
        if isinstance(movement, int):
            for _ in range(movement):
                position = move(position, direction, field)
        else:
            direction = rotate(direction, movement)

    
    return position, direction

if __name__ == "__main__":
    inputs = [user_input for user_input in read_input()]

    coordinates = [parse_input(user_input, y) for y, user_input in enumerate(inputs[:-2])]
    coordinates = sum(coordinates, [])

    current = coordinates[0][0], "R"
    coordinates = {point: type for point, type in coordinates}

    movements = inputs[-1]
    movements = parse_movements(movements)

    position, direction = moves(movements, current, coordinates)

    scoring = {
        'R': 0,
        'D': 1,
        'L': 2,
        'U': 3
    }

    print(position, direction)
    print(position.y * 1000 + position.x * 4 + scoring[direction])