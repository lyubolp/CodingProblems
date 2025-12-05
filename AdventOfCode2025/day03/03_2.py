import sys


def read_input() -> list[str]:
    return [line.strip() for line in sys.stdin]


def calculate_joltage(bank: str) -> int:

    first_digit, index = max_with_index(bank[:-1])
    second_digit, _ = max_with_index(bank[index + 1 :])

    return int(first_digit + second_digit)


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
