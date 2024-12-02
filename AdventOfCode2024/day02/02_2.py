import sys

from functools import reduce

def read_input() -> list[str]:
    return [line.strip() for line in sys.stdin]

def parse_line(line: str) -> list[int]:
    return [int(item) for item in line.split()]

def is_report_safe(report: list[int]) -> bool:
    diffs = [report[i-1] - item for i, item in enumerate(report[1:], start=1)]

    is_same_direction = all(diff > 0 for diff in diffs) or all(diff < 0 for diff in diffs)
    is_diff_enough = all(1 <= abs(diff) <= 3 for diff in diffs)

    return is_same_direction and is_diff_enough

if __name__ == "__main__":
    lines = read_input()

    numbers = [parse_line(line) for line in lines]

    are_reports_safe = [is_report_safe(report) for report in numbers]

    result = 0

    for report in numbers:
        is_base_report_safe = is_report_safe(report)

        if is_base_report_safe:
            result += 1
        else:
            for i, _ in enumerate(report):
                modified_report = report[:i] + report[i+1:]
                if is_report_safe(modified_report):
                    result += 1
                    break
                

    print(result)
