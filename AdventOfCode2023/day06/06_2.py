import sys
from functools import reduce


def read_input() -> list[str]:
    return [line.strip() for line in sys.stdin]


def parse_line(line: str) -> int:
    numbers = line.split(':')[1].strip().replace(' ', '')
    return int(numbers)


def parse_input(lines: list[str]) -> tuple[int, int]:
    return parse_line(lines[0]), parse_line(lines[1])


def calculate_possible_way_to_win(race_time: int, record_distance: int) -> int:

    distances_travaled = [(race_time - button_hold) * button_hold for button_hold in range(1, race_time)]

    return len([distance_travaled for distance_travaled in distances_travaled if distance_travaled > record_distance])


if __name__ == "__main__":
    lines = read_input()

    races = parse_input(lines)

    possible_ways_to_win = calculate_possible_way_to_win(*races)

    result = calculate_possible_way_to_win(*races)

    print(result)
