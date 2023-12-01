import sys

spelled_out_numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
                       'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}


def read_input() -> list[str]:
    return [line.strip() for line in sys.stdin]


def recover_line(line: str) -> int:
    spelled_out_indexes_start = [(index, value)
                                 for number, value in spelled_out_numbers.items()
                                 if (index := line.find(number)) != -1]

    spelled_out_indexes_end = [(index, value)
                               for number, value in spelled_out_numbers.items()
                               if (index := line.rfind(number)) != -1]

    numbers = [(i, int(char)) for i, char in enumerate(line) if char.isdigit()]

    numbers += spelled_out_indexes_start
    numbers += spelled_out_indexes_end

    numbers: list[tuple[int, int]] = sorted(numbers)

    return numbers[0][1] * 10 + numbers[-1][1]


if __name__ == "__main__":
    inputs = read_input()

    calibration_values = [recover_line(line) for line in inputs]

    result = sum(calibration_values)

    print(result)
