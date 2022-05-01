#!/usr/bin/python3

import sys
from typing import List, Tuple


def read_input() -> List[str]:
    return [line.strip() for line in sys.stdin if line != '\n']


def parse_image(lines: List[str]) -> List[List[bool]]:
    return [[True if c == '#' else False for c in line] for line in lines]


def generate_region(image: List[List[bool]], target_pixel: Tuple[int, int]) -> List[List[bool]]:
    i, j = target_pixel

    if i == 0 and j == 0:
        # top-left
        result = [[False] * 3]

        for row in image[:2]:
            result.append([False] + row[:2])

        return result
    elif i == 0 and 0 < j < len(image[0]) - 1:
        # top
        return [[False] * 3] + [row[j-1:j+2] for row in image[:2]]
    elif i == 0 and j == len(image[0]) - 1:
        # top-right
        result = [[False] * 3]

        for row in image[:2]:
            result.append(row[-2:] + [False])

        return result
    elif 0 < i < len(image) - 1 and j == len(image[0]) - 1:
        # right
        return [row[-2:] + [False] for row in image[i-1:i+2]]
    elif i == len(image) - 1 and j == len(image[0]) - 1:
        # bottom-right
        return [row[-2:] + [False] for row in image[-2:]] + [[False] * 3]
    elif i == len(image) - 1 and 0 < j < len(image[0]) - 1:
        # bottom
        return [row[j - 1:j + 2] for row in image[-2:]] + [[False] * 3]
    elif i == len(image) - 1 and j == 0:
        # bottom-left
        return [[False] + row[:2] for row in image[-2:]] + [[False] * 3]
    elif 0 < i < len(image) - 1 and j == 0:
        # left
        return [[False] + row[:2] for row in image[i - 1:i + 2]]
    else:
        return [row[j - 1: j + 2] for row in image[i - 1:i + 2]]


def region_to_int(region: List[List[bool]]) -> int:
    result_str = "".join(['1' if item else '0' for item in sum(region, [])])
    return int(result_str, base=2)


def enhance_pixel(algorithm: str, image: List[List[bool]], target_pixel: Tuple[int, int]) -> bool:
    region = generate_region(image, target_pixel)
    algorithm_index = region_to_int(region)

    return True if algorithm[algorithm_index] == '#' else False


def enhance(algorithm: str, image: List[List[bool]]) -> List[List[bool]]:
    return [[enhance_pixel(algorithm, image, (i, j)) for j in range(len(image[0]))] for i in range(len(image))]


def pretty_print(image: List[List[bool]]):
    for row in image:
        print("".join(['#' if item else '.' for item in row]))


if __name__ == "__main__":
    lines = read_input()

    algorithm = lines[0]
    image = parse_image(lines[1:])

    # print(algorithm)
    # print(image)

    after_one = enhance(algorithm, image)
    # pretty_print(after_one)

    after_two = enhance(algorithm, after_one)
    # pretty_print(after_two)

    print(sum(sum([[1 for item in row if item]for row in after_two], [])))
