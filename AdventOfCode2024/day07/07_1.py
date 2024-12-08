import sys


def read_input() -> list[str]:
    return [line.strip() for line in sys.stdin]


def parse_line(line: str) -> tuple[int, list[int]]:
    target_value, numbers = line.split(':')
    return int(target_value), [int(number) for number in numbers.split()]


def is_equation_true(equation: tuple[int, list[int]]) -> bool:
    target, numbers = equation

    stack = [(target, numbers[::])]

    while len(stack) > 0:
        current_target, current_numbers = stack.pop()
        if current_target == 0:
            return True
        elif current_target < 0:
            continue
        elif len(current_numbers) == 0:
            continue

        if current_target % current_numbers[-1] == 0:
            stack.append((current_target // current_numbers[-1], current_numbers[:-1]))

        stack.append((current_target - current_numbers[-1], current_numbers[:-1]))

    return False


if __name__ == "__main__":
    lines = read_input()

    equations = [parse_line(line) for line in lines]

    valid_equations = [equation for equation in equations if is_equation_true(equation)]

    print(valid_equations)
    print(sum(target for target, _ in valid_equations))

