import os
import sys

from typing import Dict, List, Tuple

def read_input() -> List[str]:
    return [line for line in sys.stdin]


def split_input(input: List[str]) -> List[List[int]]:
    return [[int(c) for c in line] for line in input]

def get_tree_scenic_score_left(tree_coord: Tuple[int, int], trees: List[List[int]]) -> int:
    i, j = tree_coord
    max_offset = j + 1
    for offset in range(1, max_offset):
        if trees[i][j - offset] >= trees[i][j]:
            return offset

    return max_offset - 1


def get_tree_scenic_score_right(tree_coord: Tuple[int, int], trees: List[List[int]]) -> int:
    i, j = tree_coord
    max_offset = len(trees[i]) - j
    for offset in range(1, max_offset):
        if trees[i][j + offset] >= trees[i][j]:
            return offset

    return max_offset - 1


def get_tree_scenic_score_top(tree_coord: Tuple[int, int], trees: List[List[int]]) -> int:
    i, j = tree_coord
    max_offset = i + 1
    for offset in range(1, max_offset):
        if trees[i - offset][j] >= trees[i][j]:
            return offset

    return max_offset - 1


def get_tree_scenic_score_bottom(tree_coord: Tuple[int, int], trees: List[List[int]]) -> int:
    i, j = tree_coord
    max_offset = len(trees[j]) - i
    for offset in range(1, max_offset):
        if trees[i + offset][j] >= trees[i][j]:
            return offset

    return max_offset - 1


def get_tree_scenic_score(tree_coord: Tuple[int, int], trees: List[List[int]]) -> int:
    i, j = tree_coord
    tree = trees[i][j]

    left = get_tree_scenic_score_left(tree_coord, trees)
    right = get_tree_scenic_score_right(tree_coord, trees)
    top = get_tree_scenic_score_top(tree_coord, trees)
    bottom = get_tree_scenic_score_bottom(tree_coord, trees)

    return left * right * top * bottom

if __name__ == "__main__":
    inputs = [user_input.strip() for user_input in read_input()]
    trees = split_input(inputs)

    scores = sum([[get_tree_scenic_score((i, j), trees) for j, _ in enumerate(row)] for i, row in enumerate(trees)], [])
    print(max(scores))