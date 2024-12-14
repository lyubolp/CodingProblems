import re
import sys

input_re = re.compile(r".*X[+=]([0-9]*), Y[+=]([0-9]*).*")


def read_input() -> list[str]:
    return [line.strip() for line in sys.stdin]


def parse_input(line: str) -> tuple[int, int]:
    return int(input_re.match(line).group(1)), int(input_re.match(line).group(2))


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
    for button_a, button_b, prize in parsed:
        prize = prize[0], prize[1]
        prize = prize[0] + 10000000000000, prize[1] + 10000000000000

        b = ((prize[0] * button_a[1]) - (prize[1] * button_a[0])) / ((button_b[0]*button_a[1]) - (button_b[1]*button_a[0]))
        a = (prize[0] - (button_b[0] * b)) / button_a[0]

        if float(int(a)) == a and float(int(b)) == b:
            print(a, b)
            result += int(calculate_tokens(a, b))
        else:
            print("Not possible")

    print(result)
