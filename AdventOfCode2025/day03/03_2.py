import sys


def read_input() -> list[str]:
    return [line.strip() for line in sys.stdin]


def calculate_joltage(bank: str) -> int:
    max_digits = 12
    digits = []

    start = 0
    for digits_taken in range(max_digits):
        end = max_digits - digits_taken - 1

        if end == 0:
            digits.append(max(bank[start:]))
            # print(max(bank[start:]))
            continue
        digit, new_start = max_with_index(bank[start:-end])
        # print(start, end, bank[start:-end], digit)
        digits.append(digit)
        start += new_start + 1

    return int("".join(digits))


def max_with_index(bank: str) -> tuple[str, int]:
    current_max = "0"
    max_index = -1
    for i, c in enumerate(bank):
        if c > current_max:
            current_max = c
            max_index = i

    return current_max, max_index


if __name__ == "__main__":
    lines = read_input()

    joltages = [calculate_joltage(line) for line in lines]
    print(joltages)
    print(sum(joltages))

    # print(calculate_joltage(lines[1]))
