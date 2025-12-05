import sys


def read_input() -> list[str]:
    return [line.strip() for line in sys.stdin]


def parse_lines(lines: list[str]) -> list[tuple[int, int]]:
    raw_ranges = [item.split("-") for item in lines[0].split(",")]
    return [(int(raw_start), int(raw_end)) for raw_start, raw_end in raw_ranges]


def is_id_invalid(_id: int) -> bool:
    id_as_str = str(_id)
    length = len(id_as_str)

    mid = length // 2

    for i in range(1, mid + 1):
        if len(split_string_in_pieces(id_as_str, i)) == 1:
            return True

    return False


def split_string_in_pieces(item: str, length: int) -> set[str]:
    if len(item) % length != 0:
        return set()

    max_pieces = len(item) // length

    result = set()

    for i in range(max_pieces):
        start = i * length
        end = (i + 1) * length
        result.add(item[start:end])

    return result


if __name__ == "__main__":
    lines = read_input()

    ranges = parse_lines(lines)

    result = 0
    for start, end in ranges:
        for _id in range(start, end + 1):
            if is_id_invalid(_id):
                # print(_id)
                result += _id

    print(f"{result=}")
