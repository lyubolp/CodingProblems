import math
import sys


def read_input() -> list[str]:
    return [line.strip() for line in sys.stdin]


def parse_line(line: str) -> tuple[int, list[int]]:
    target_value, numbers = line.split(':')
    return int(target_value), [int(number) for number in numbers.split()]


def is_equation_true(equation: tuple[int, list[int]]) -> bool:
    target, numbers = equation

    stack = [(numbers[0], numbers[1:])]

    while len(stack) > 0:
        current_target, current_numbers = stack.pop()
        if current_target == target and len(current_numbers) == 0:
            return True
        elif current_target > target:
            continue
        elif len(current_numbers) == 0:
            continue

        stack.append((current_target * current_numbers[0], current_numbers[1:]))
        stack.append((current_target + current_numbers[0], current_numbers[1:]))
        stack.append((concat_two_numbers(current_target, current_numbers[0]), current_numbers[1:]))

    return False


def concat_two_numbers(first: int, second: int) -> int:
    second_len = int(math.log10(second)) + 1

    return first * (10 ** second_len) + second


if __name__ == "__main__":
    lines = read_input()

    equations = [parse_line(line) for line in lines]

    valid_equations = [equation for equation in equations if is_equation_true(equation)]

    # print(valid_equations)
    print(sum(target for target, _ in valid_equations))

