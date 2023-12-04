import sys


def read_input() -> list[str]:
    return [line.strip() for line in sys.stdin]


def parse_card(line: str) -> tuple[set[int], set[int]]:
    numbers = line.split(':')[1].strip().split('|')

    my_numbers = numbers[0].strip().split()
    winning_numbers = numbers[1].strip().split()

    return set(cast_list_of_numbers(my_numbers)),  set(cast_list_of_numbers(winning_numbers))


def cast_list_of_numbers(nunbers: list[str]) -> list[int]:
    return [int(number) for number in nunbers]


def calculate_points(my_numbers: set[int], winning_numbers: set[int]) -> int:
    overlap = my_numbers & winning_numbers

    return 2 ** (len(overlap) - 1) if len(overlap) > 0 else 0


if __name__ == "__main__":
    lines = read_input()

    numbers = [parse_card(line) for line in lines]

    points = [calculate_points(my, winning) for (my, winning) in numbers]

    result = sum(points)

    print(result)
