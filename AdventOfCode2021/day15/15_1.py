#!/usr/bin/python3
import sys
from typing import List, Tuple, Dict, Set
from queue import PriorityQueue

def read_input() -> List[str]:
    return [line.strip() for line in sys.stdin if line != '\n']


def parse_input(lines: List[str]) -> List[List[int]]:
    return [[int(c) for c in line] for line in lines]


def init_scores(risk_levels: List[List[int]]) -> Dict[Tuple[int, int], int]:
    result = {}

    for i in range(len(risk_levels)):
        for j in range(len(risk_levels[0])):
            result[(i, j)] = 100000000000000000

    result[(0, 0)] = 0

    return result


def init_unvisited(risk_levels: List[List[int]]) -> Set[Tuple[int, int]]:
    result = set()

    for i in range(len(risk_levels)):
        for j in range(len(risk_levels[0])):
            result.add((i, j))

    return result


def get_neighbours(current: Tuple[int, int], risk_levels: List[List[int]]) -> List[Tuple[int, int]]:
    current_i, current_j = current
    offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    result = []
    for offset_i, offset_j in offsets:
        target_i, target_j = current_i + offset_i, current_j + offset_j

        if 0 <= target_i < len(risk_levels) and 0 <= target_j < len(risk_levels[0]):
            result.append((target_i, target_j))

    return result


def dijkstra(risk_levels: List[List[int]], start_node: Tuple[int, int], target_node: Tuple[int, int]) -> int:
    unvisited = init_unvisited(risk_levels)

    scores = init_scores(risk_levels)

    while len(unvisited) > 0:
        # Sort unvisited nodes scores
        node_scores = [(node, scores[node]) for node in scores if node in unvisited]

        # Get the pair with the lowest code, and from it get the node
        current = min(node_scores, key=lambda x: x[1])[0]

        unvisited.remove(current)

        if current == target_node:
            return scores[current]

        for neighbour in get_neighbours(current, risk_levels):
            if neighbour in unvisited:
                current_score = scores[current] + risk_levels[neighbour[0]][neighbour[1]]
                if current_score <= scores[neighbour]:
                    scores[neighbour] = current_score

    return -1


if __name__ == "__main__":
    risk_levels = parse_input(read_input())

    score = dijkstra(risk_levels, (0, 0), (len(risk_levels) - 1, len(risk_levels[0]) - 1))

    print(score)
