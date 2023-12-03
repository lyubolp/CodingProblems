import sys
from collections import namedtuple

Matrix = list[list[str]]
Point = namedtuple('Point', ['i', 'j'])


def read_input() -> list[str]:
    """
    Read the full input from the stdin, and format it as a list
    :return: A list with each of the lines in the input
    """
    return [line.strip() for line in sys.stdin]


def is_number_adjacent_to_a_symbol(matrix: Matrix, start: Point, end: Point) -> bool:
    """
    Checks if a number (represented by a range) in the matrix is adjacent to a symbol
    :param matrix: the input matrix
    :param start: the start of the number as a Point
    :param end: the end of the number as a Point
    :return: If the number has an ajdacent symbol
    """
    offsets_i = [-1, 0, 1]

    for offset_i in offsets_i:
        for current_j in range(start.j - 1, end.j + 1):
            current_i = start.i + offset_i
            if is_coordinate_in_bounds(matrix, current_i, current_j) and is_content_symbol(matrix[current_i][current_j]):
                return True

    return False


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


def read_number(matrix: Matrix, start: Point, end: Point) -> int:
    """
    Extract the number from the matrix, from a given start and end points.
    """
    return int(matrix[start.i][start.j:end.j])


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

        # Corner case handled here
        if number_start is not None:
            numbers_locations.append((number_start, Point(i, j+1)))
            number_start = None

    numbers_which_have_adjacent_symbol = [read_number(lines, *location)
                                          for location in numbers_locations
                                          if is_number_adjacent_to_a_symbol(lines, *location)]

    result = sum(numbers_which_have_adjacent_symbol)
    print(result)
