import re
import sys

regex = re.compile(r"(don't)|(do)|(mul\((\d*),(\d*)\))")

def read_input() -> list[str]:
    return [line.strip() for line in sys.stdin]


def extract_args_from_line(line: str) -> tuple[int, int]:
    results = []
    is_dont_active = False
    for dont, do, _, arg1, arg2 in regex.findall(line):
        if dont != '':
            is_dont_active = True
        elif do != '':
            is_dont_active = False
        else:
            if not is_dont_active:
                results.append((int(arg1), int(arg2)))

    return results

if __name__ == "__main__":
    lines = read_input()

    line = "".join(lines)
    args = extract_args_from_line(line)

    results = [(arg1 * arg2) for arg1, arg2 in args]
    print(sum(results))

