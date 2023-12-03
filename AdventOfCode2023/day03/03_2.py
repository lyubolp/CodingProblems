import sys
from collections import namedtuple
from typing import Optional


Matrix = list[list[str]]
Point = namedtuple('Point', ['i', 'j'])


def read_input() -> list[str]:
    """
    Read the full input from the stdin, and format it as a list
    :return: A list with each of the lines in the input
    """
    return [line.strip() for line in sys.stdin]


def is_number_adjacent_to_a_star(matrix: Matrix, start: Point, end: Point) -> Optional[Point]:
    """
    Checks if a number (represented by a range) in the matrix is adjacent to a '*'
    :param matrix: the input matrix
    :param start: the start of the number as a Point
    :param end: the end of the number as a Point
    :return: The location of the '*', if it exists
    """
    offsets_i = [-1, 0, 1]

    for offset_i in offsets_i:
        for current_j in range(start.j - 1, end.j + 1):
            current_i = start.i + offset_i
            if is_coordinate_in_bounds(matrix, current_i, current_j) and matrix[current_i][current_j] == '*':
                return Point(current_i, current_j)

    return None


def is_coordinate_in_bounds(matrix: Matrix, i: int, j: int) -> bool:
    """
    Checks if a coordinate is within the matrix bounds
    :param matrix: The matrix to check against
    :param i: The first coordinate
    :param j: The second coordinate
    :return: If the coordinate is within the matrix
    """
    return 0 <= i < len(matrix) and 0 <= j < len(matrix[0])


def is_content_symbol(content: str) -> bool:
    """
    A symbol is not strictly defined, but we know it's not a number or a dot
    """
    return not content.isnumeric() and content != '.'


if __name__ == "__main__":
    lines = read_input()

    number_start = None
    numbers_locations = []

    # Iterate over the input matrix
    # For each character:
    #   if it's a digit, check if it's a new number or part of an existing one
    #   If it's not a digit, this means that the number has ended
    # A corner case is when the digit ends with the line
    for i, row in enumerate(lines):
        for j, item in enumerate(row):
            if not item.isnumeric():
                if number_start is not None:
                    numbers_locations.append((number_start, Point(i, j)))
                    number_start = None
            else:
                if number_start is None:
                    number_start = Point(i, j)
        if number_start is not None:
            numbers_locations.append((number_start, Point(i, j+1)))
            number_start = None

    # Get the numbers and their respective stars
    numbers_which_have_adjacent_star = [(adj_star, read_number(lines, *location))
                                        for location in numbers_locations
                                        if (adj_star := is_number_adjacent_to_a_star(lines, *location)) is not None]

    # Mapping out stars to numbers
    adjacent_star_to_numbers = {}   
    for adj_star, number in numbers_which_have_adjacent_star:
        if adj_star not in adjacent_star_to_numbers:
            adjacent_star_to_numbers[adj_star] = [number]
        else:
            adjacent_star_to_numbers[adj_star].append(number)

    gear_ratios = [numbers for numbers in adjacent_star_to_numbers.values() if len(numbers) == 2]

    # We know that ratios has only 2 elements
    result = sum(map(lambda ratios: ratios[0] * ratios[1], gear_ratios))
    print(result)
