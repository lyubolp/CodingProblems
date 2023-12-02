import sys
from collections import UserDict


possible_values = {'blue': 14, 'green': 13, 'red': 12}


def read_input() -> list[str]:
    return [line.strip() for line in sys.stdin]


class CubeDraw(UserDict):
    def __init__(self, blue: int = 0, green: int = 0, red: int = 0):
        super().__init__()
        self.data['blue'] = blue
        self.data['green'] = green
        self.data['red'] = red

    def is_cube_draw_possible(self) -> bool:
        return all(self.data[color] <= possible_values[color] for color in self.data)

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


def are_cube_draws_possible(cube_sets: list[CubeDraw]) -> bool:
    return all(cube_set.is_cube_draw_possible() for cube_set in cube_sets)


if __name__ == "__main__":
    lines = read_input()

    games = [(i+1, parse_game_line(line)) for i, line in enumerate(lines)]

    games = [(game_id, cube_draws) for (game_id, cube_draws) in games if are_cube_draws_possible(cube_draws)]

    result = sum(game_id for (game_id, _) in games)

    print(result)
