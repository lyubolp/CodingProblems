#!/usr/bin/python3
import sys
from typing import List, Tuple, Dict, Set


def read_input() -> List[str]:
    return [line.strip() for line in sys.stdin if line != '\n']


def build_adj_list(lines: List[str]) -> Dict[str, List[str]]:
    result = {}
    for line in lines:
        start, end = line.split('-')

        if start in result:
            result[start].append(end)
        else:
            result[start] = [end]

        if end in result:
            result[end].append(start)
        else:
            result[end] = [start]

    return result


def dfs(adj_list: Dict[str, List[str]], current: str, visited: Dict[str, int], path: List[str], paths: List[List[str]], is_double_visit_done: bool):
    if current.islower():
        if current in visited:
            visited[current] += 1
        else:
            visited[current] = 1

    path.append(current)

    if current == 'end':
        paths.append(path.copy())
    else:
        for neighbour in adj_list[current]:
            if neighbour == 'start':
                continue

            if neighbour not in visited or visited[neighbour] < 1:
                dfs(adj_list, neighbour, visited, path, paths, is_double_visit_done)
            elif visited[neighbour] < 2 and not is_double_visit_done:
                dfs(adj_list, neighbour, visited, path, paths, True)


    path.pop()
    if current.islower():
        visited[current] -= 1


if __name__ == "__main__":
    lines = read_input()
    adj_list = build_adj_list(lines)

    paths = []
    dfs(adj_list, "start", {}, [], paths, False)

    print(len(paths))