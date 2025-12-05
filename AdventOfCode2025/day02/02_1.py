import sys


def read_input() -> list[str]:
    return [line.strip() for line in sys.stdin]


def parse_lines(lines: list[str]) -> list[tuple[int, int]]:
    raw_ranges = [item.split("-") for item in lines[0].split(",")]
    return [(int(raw_start), int(raw_end)) for raw_start, raw_end in raw_ranges]


def is_id_invalid(id: int) -> bool:
    id_as_str = str(id)
    length = len(id_as_str)

    if length % 2 == 1:
        return False

    mid = length // 2
    return id_as_str[:mid] == id_as_str[mid:]


if __name__ == "__main__":
    lines = read_input()

    ranges = parse_lines(lines)

    result = 0
    for start, end in ranges:
        for _id in range(start, end + 1):
            if is_id_invalid(_id):
                print(_id)
                result += _id

    print(f"{result=}")
