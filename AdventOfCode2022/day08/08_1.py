import os
import sys

from typing import Dict, List, Tuple

def read_input() -> List[str]:
    return [line for line in sys.stdin]


def split_input(input: List[str]) -> List[List[int]]:
    return [[int(c) for c in line] for line in input]


def is_tree_visible(tree_coord: Tuple[int, int], trees: List[List[int]]) -> bool:
    i, j = tree_coord
    tree = trees[i][j]

    is_visible_left = max(trees[i][:j]) < tree
    is_visible_right = max(trees[i][j+1:]) < tree
    is_visible_top = max(trees[row][j] for row in range(i)) < tree
    is_visible_bottom = max(trees[row][j] for row in range(i+1,  len(trees[0]))) < tree

    return is_visible_left or is_visible_right or is_visible_top or is_visible_bottom

if __name__ == "__main__":
    inputs = [user_input.strip() for user_input in read_input()]
    trees = split_input(inputs)

    visible_trees = trees[0] + trees[-1] 
    visible_trees += [trees[row][0] for row in range(1, len(trees) - 1)] 
    visible_trees += [trees[row][-1] for row in range(1, len(trees) - 1)]
    visible_trees += sum([
        [trees[i][j] for j in range(1, len(trees[0]) - 1) if is_tree_visible((i, j), trees)] 
        for i in range(1, len(trees) - 1)], [])


    print(len(visible_trees))