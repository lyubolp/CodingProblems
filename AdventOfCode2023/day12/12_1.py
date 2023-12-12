import math
import sys


def read_input() -> list[str]:
    return [line.strip() for line in sys.stdin]


def parse_contiguous_group_info(info: str) -> list[int]:
    return [int(value) for value in info.split(',')]


def calculate_permutations(n: int, r: int) -> int:
    return int(math.factorial(n) / math.factorial(n - r))


def is_arrangment_matching(arrangement: str, group_info: list[int]) -> bool:
    groups = [group for group in arrangement.split('.') if group != '']

    if len(groups) != len(group_info):
        return False

    group_counts = [group.count('#') for group in groups]

    return group_counts == group_info


def permute_arrangement(start: str, counts: list[int]) -> list[str]:
    stack = [start]
    max_damaged = sum(counts)
    results = []
    while len(stack) > 0:
        current = stack.pop()

        # print(current)
        unknown_count = current.count('?')

        if unknown_count == 0:
            results.append(current)
            continue

        bad_count = current.count('#')

        if bad_count > max_damaged or bad_count + unknown_count < max_damaged:
            continue

        groups = [group for group in current.split('.') if group != '']

        is_valid = True
        for i, group in enumerate(groups):
            if '?' in group:
                break

            if i >= len(counts):
                break

            if len(group) != counts[i]:
                is_valid = False

        if not is_valid:
            continue

        candidate_1 = current.replace('?', '#', 1)
        candidate_2 = current.replace('?', '.', 1)

        stack += [candidate_1, candidate_2]

    return results


if __name__ == "__main__":
    lines = read_input()
    lines = [line.split() for line in lines]

    lines = [(line, parse_contiguous_group_info(grouping)) for line, grouping in lines]

    results = [
        [1 for permutation in permute_arrangement(line, grouping)
         if is_arrangment_matching(permutation, grouping)]
        for line, grouping in lines
    ]

    results = [sum(permutations) for permutations in results]
    result = sum(results)
    print(result)

    permute_arrangement('?###????????', [3, 2, 1])
