import sys


def read_input() -> list[str]:
    return [line.strip() for line in sys.stdin]


def parse_input(lines: list[str]) -> tuple[list[tuple[int, int]], list[int]]:
    ranges = [tuple(line.split("-")) for line in lines if "-" in line]
    ranges = [(int(start), int(end)) for (start, end) in ranges]
    items = [int(line) for line in lines if "-" not in line and line != ""]

    return sorted(ranges, key=lambda item: (item[0], item[1])), items


def merge_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    result = []

    current = ranges[0]

    for new_range in ranges:
        if new_range[0] <= current[1]:
            current = current[0], max(current[1], new_range[1])
        else:
            result.append(current)
            current = new_range

    result.append(current)
    return result


def get_ranges_length(ranges: list[tuple[int, int]]) -> int:
    return sum(current[1] - current[0] + 1 for current in ranges)


if __name__ == "__main__":
    lines = read_input()
    ranges, _ = parse_input(lines)
    merged_ranges = merge_ranges(ranges)

    print(len(ranges))
    # print(merged_ranges)
    result = get_ranges_length(merged_ranges)
    print(result)

    # ranges = [(5, 13), (8, 12)]
    # print(merge_ranges(ranges))
