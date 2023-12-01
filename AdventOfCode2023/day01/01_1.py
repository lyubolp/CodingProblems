import sys


def read_input() -> list[str]:
    return [line.strip() for line in sys.stdin]


def recover_line(line: str) -> int:
    numbers = [char for char in line if char.isdigit()]

    return int(numbers[0] + numbers[-1])


if __name__ == "__main__":
    inputs = read_input()

    calibration_values = [recover_line(line) for line in inputs]

    result = sum(calibration_values)
    print(result)
