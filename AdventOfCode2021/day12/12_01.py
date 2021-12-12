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

def dfs(adj_list: Dict[str, List[str]], current: str, visited: Dict[str, bool], path: List[str], paths: List[List[str]]):
    if current.islower():
        visited[current] = True
    path.append(current)

    if current == 'end':
        paths.append(path.copy())
    else:
        for neighbour in adj_list[current]:
            if neighbour not in visited or visited[neighbour] == False:
                dfs(adj_list, neighbour, visited, path, paths)
    
    path.pop()
    visited[current] = False

if __name__ == "__main__":
    lines = read_input()
    adj_list = build_adj_list(lines)

    paths = []
    dfs(adj_list, "start", {}, [], paths)

    print(len(paths))