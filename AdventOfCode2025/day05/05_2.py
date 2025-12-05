import sys


def read_input() -> list[str]:
    return [line.strip() for line in sys.stdin]


def parse_input(lines: list[str]) -> tuple[list[tuple[int, int]], list[int]]:
    ranges = [tuple(line.split("-")) for line in lines if "-" in line]
    ranges = [(int(start), int(end)) for (start, end) in ranges]
    items = [int(line) for line in lines if "-" not in line and line != ""]

    return ranges, items


def merge_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    result = []

    for new_start, new_end in sorted(ranges):
        pass
    return result


def merge_range(new_range: tuple[int, int], current: list[tuple[int, int]]) -> list[tuple[int, int]]:
    new_ranges = []

    new_start, new_end =  new_range

    for current_start, current_end in current:
        if current_end < new_start:
            new_ranges.append((current_start, current_end))
        pass
    
    return new_ranges


if __name__ == "__main__":
    lines = read_input()
    ranges, _ = parse_input(lines)

    print(list(sorted(ranges)))
