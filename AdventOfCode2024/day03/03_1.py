import re
import sys

regex = re.compile(r"(mul\((\d*),(\d*)\))")

def read_input() -> list[str]:
    return [line.strip() for line in sys.stdin]


def extract_args_from_line(line: str) -> tuple[int, int]:
    return [(int(arg1), int(arg2)) for _, arg1, arg2 in regex.findall(line)]

if __name__ == "__main__":
    lines = read_input()

    args = sum([extract_args_from_line(line) for line in lines], [])

    results = [(arg1 * arg2) for arg1, arg2 in args]
    print(sum(results))

