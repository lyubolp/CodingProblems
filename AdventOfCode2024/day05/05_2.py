import sys

from collections import defaultdict
from functools import cmp_to_key


def read_input() -> list[str]:
    return [line.strip() for line in sys.stdin]


def parse_update(update: str) -> list[int]:
    return [int(item) for item in update.split(",")]


def parse_rule(rule: str) -> tuple[int, int]:
    splitted = rule.split("|")
    return int(splitted[0]), int(splitted[1])


def is_update_valid(update: list[int], rules: list[tuple[int, int]]) -> bool:
    for i, page in enumerate(update):
        if not all(item in rules[page] for item in update[i + 1 :]):
            return False

    return True


def sort_update(update: list[int], rules: defaultdict[int, set]) -> list[int]:
    return sorted(update, key=lambda page: rank_page(page, update, rules), reverse=True)


def rank_page(page: int, update: list[int], rules: defaultdict[int, set]) -> int:
    return sum(1 for other_page in update if other_page != page and other_page in rules[page])


if __name__ == "__main__":
    lines = read_input()

    for i, line in enumerate(lines):
        if line == "":
            all_rules = [parse_rule(rule) for rule in lines[:i]]

            rules = defaultdict(set)

            for start, end in all_rules:
                rules[start].add(end)

            updates = [parse_update(update) for update in lines[i + 1 :]]
            break

    sorted_updates = [
        sort_update(update, rules)
        for update in updates
        if not is_update_valid(update, rules)
    ]

    print(sorted_updates)

    middles = [update[len(update) // 2] for update in sorted_updates]
    print(sum(middles))
