import sys
from collections import defaultdict
from functools import reduce


def read_input() -> list[str]:
    return [line.strip() for line in sys.stdin]


def hash_algorithm(sequence: str) -> int:
    return reduce(hash_algorithm_character, sequence, 0)


def hash_algorithm_character(start_value: int, character: str) -> int:
    return ((start_value + ord(character)) * 17) % 256


def remove_lens_from_box(box: list[tuple[str, int]], lens_to_remove: str) -> list[tuple[str, int]]:
    indexes_to_remove = set(i for i, (lens, _) in enumerate(box) if lens == lens_to_remove)

    return [item for i, item in enumerate(box) if i not in indexes_to_remove]


def add_lens_to_box(box: list[tuple[str, int]], lens_to_add: tuple[str, int]) -> list[tuple[str, int]]:

    new_box = []
    has_added = False

    for lens, focal_length in box:
        if lens == lens_to_add[0]:
            new_box.append((lens, lens_to_add[1]))
            has_added = True
        else:
            new_box.append((lens, focal_length))

    if not has_added:
        new_box.append(lens_to_add)

    return new_box


if __name__ == "__main__":
    lines = read_input()
    sequences = lines[0].split(',')

    boxes = defaultdict(list)
    for sequence in sequences:
        if '=' in sequence:
            label, focal_length = sequence.split('=')
            focal_length = int(focal_length)
        if '-' in sequence:
            label, _ = sequence.split('-')

        hashed_label = hash_algorithm(label)

        if '=' in sequence:
            boxes[hashed_label] = add_lens_to_box(boxes[hashed_label], (label, focal_length))

        if '-' in sequence:
            boxes[hashed_label] = remove_lens_from_box(boxes[hashed_label], label)

    results = []
    for box_id in boxes:
        for i, (lens, focal_length) in enumerate(boxes[box_id]):
            results.append((box_id + 1) * (i + 1) * focal_length)

    result = sum(results)
    print(result)
    # print(boxes)
