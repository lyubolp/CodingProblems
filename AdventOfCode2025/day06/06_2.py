import sys

from functools import reduce


def read_input() -> list[str]:
    return [line[:-1] for line in sys.stdin]


def parse_input(lines: list[str], separators: list[int]) -> list[list[str]]:
    result = []

    for i, separator_index in enumerate(separators[:-1]):
        start = separator_index
        end = separators[i + 1]
        result.append([line[start:end] for line in lines])

    result.append([line[separators[-1] :] for line in lines])

    return result


def parse_line(line: list[str]) -> list[int]:
    results = []

    for i in range(len(line[0])):
        digit = "".join(number[i] for number in line if number != " ")
        results.append(digit)
    return [int(result) for raw_result in results if (result := raw_result.strip()) != ""]


def evaluate_numbers(items: list[int], operation: str) -> int:
    if operation == "+":
        return sum(items)
    elif operation == "*":
        return reduce(lambda acc, item: acc * item, items, 1)
    return 0


if __name__ == "__main__":
    lines = read_input()

    column_separators = [i for i, c in enumerate(lines[-1]) if c != " "]

    table = parse_input(lines, column_separators)

    result = 0
    for line in table:
        operation = line[-1].strip()
        numbers = parse_line(line[:-1])
        current_result = evaluate_numbers(numbers, operation)
        print(f"{numbers} = {current_result}")
        result += current_result

    print(result)
