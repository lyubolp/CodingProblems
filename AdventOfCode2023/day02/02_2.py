import sys
from collections import UserDict
from functools import reduce


possible_values = {'blue': 14, 'green': 13, 'red': 12}


def read_input() -> list[str]:
    return [line.strip() for line in sys.stdin]


class CubeDraw(UserDict):
    def __init__(self, blue: int = 0, green: int = 0, red: int = 0):
        super().__init__()
        self.data['blue'] = blue
        self.data['green'] = green
        self.data['red'] = red

    @staticmethod
    def from_raw_input(line: str):
        cube_counts = line.split(', ')
        cube_counts = [cube_count.strip() for cube_count in cube_counts]

        cube_counts_colors = [cube_count.split(' ') for cube_count in cube_counts]

        return CubeDraw(**{color: int(count) for count, color in cube_counts_colors})


def parse_game_line(line: str) -> list[CubeDraw]:
    sets = line.split(':')[1].split(';')
    sets = [item.strip() for item in sets]

    return [CubeDraw.from_raw_input(cube_set) for cube_set in sets]


def calculate_minimal_amount_of_cubes(cube_sets: list[dict[str, int]]) -> dict[str, int]:
    result = {'blue': 0, 'green': 0, 'red': 0}

    for cube_set in cube_sets:
        for color, count in cube_set.items():
            result[color] = max(result[color], count)

    return result


def power_of_cube_set(cube_set: dict[str, int]) -> int:
    return reduce(lambda x, y: x * y, cube_set.values(), 1)


if __name__ == "__main__":
    lines = read_input()

    cube_sets = [(i+1, parse_game_line(line)) for i, line in enumerate(lines)]

    amount_of_cubes = [calculate_minimal_amount_of_cubes(cube_set) for _, cube_set in cube_sets]

    result = sum(power_of_cube_set(cube_set) for cube_set in amount_of_cubes)
    print(result)
