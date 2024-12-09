import sys


def read_input() -> list[str]:
    return [line.strip() for line in sys.stdin]


def generate_layout(disk_map: str) -> list[list[str, int]]:
    result = []

    current_id = 0
    for i, digit in enumerate(disk_map):
        if i % 2 == 0:
            result.append([current_id, int(digit)])
            current_id += 1
        else:
            result.append([".", int(digit)])
    return result


def reorder_files(files: list[list[str, int]]) -> list[list[str, int]]:
    result = [files[0]]

    left_block = 2
    current_free_space = 1
    current_block = len(files) - 1

    while current_block > current_free_space:
        space_left = files[current_free_space][1]
        space_required = files[current_block][1]

        if space_left > space_required:
            # Enough space
            result.append(files[current_block])
            files[current_free_space][1] -= files[current_block][1]

            current_block -= 2
        elif space_left == space_required:
            # Just enough space

            result.append(files[current_block])

            if current_block != left_block:
                result.append(files[left_block])

            current_block -= 2
            current_free_space += 2
            left_block += 2

        else:
            # Not enough space
            files[current_block][1] -= space_left
            result.append([files[current_block][0], space_left])
            result.append(files[left_block])

            current_free_space += 2
            left_block += 2

    return result


def is_partitioned_properly(files: list[str], first_dot: list[int]) -> bool:
    return all(c == "." for c in files[first_dot:])


def pretty_print(files: list[tuple[str, int]]) -> str:
    expanded = []

    for symbol, amount in files:
        expanded += [str(symbol)] * amount

    return "".join(expanded)


if __name__ == "__main__":
    lines = read_input()
    disk_map = lines[0]

    disk_layout = generate_layout(disk_map)
    reordered_layout = reorder_files(disk_layout)

    summable = sum([[file_id] * count for file_id, count in reordered_layout], [])
    print(sum(i * file_id for i, file_id in enumerate(summable)))
