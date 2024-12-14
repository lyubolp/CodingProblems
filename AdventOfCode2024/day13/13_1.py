import re
import sys

input_re = re.compile(r".*X[+=]([0-9]*), Y[+=]([0-9]*).*")


def read_input() -> list[str]:
    return [line.strip() for line in sys.stdin]


def parse_input(line: str) -> tuple[int, int]:
    return int(input_re.match(line).group(1)), int(input_re.match(line).group(2))


def calculate_combos(button_a, button_b, prize) -> list[tuple]:
    result = []
    for a_presses in range(101):
        a_x_offset = button_a[0] * a_presses
        b_x_offset = prize[0] - a_x_offset

        if b_x_offset % button_b[0] != 0:
            continue

        b_presses = b_x_offset // button_b[0]

        a_y_offset = button_a[1] * a_presses
        b_y_offset = button_b[1] * b_presses

        if a_y_offset + b_y_offset == prize[1]:
            result.append((a_presses, b_presses))

    return result


def calculate_tokens(a_presses, b_presses) -> int:
    return 3 * a_presses + b_presses


if __name__ == "__main__":
    lines = read_input()

    lines_iter = iter(lines)

    parsed = []
    try:
        while True:
            button_a = next(lines_iter)
            button_b = next(lines_iter)
            prize = next(lines_iter)

            button_a_parsed = parse_input(button_a)
            button_b_parsed = parse_input(button_b)
            prize_parsed = parse_input(prize)

            parsed.append((button_a_parsed, button_b_parsed, prize_parsed))

            _ = next(lines_iter)  # Empty line
    except StopIteration:
        pass

    result = 0
    for button_a, button_b, prize in parsed[-1:]:
        print(button_a, button_b, prize)
        combos = calculate_combos(button_a, button_b, prize)
        if len(combos) > 0:
            print(combos[0])
        else:
            print("Not possible")
        result += min(calculate_tokens(*combo) for combo in combos) if len(combos) > 0 else 0

    print(result)
