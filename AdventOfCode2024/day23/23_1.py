import sys

from collections import defaultdict
from functools import reduce


def read_input() -> list[str]:
    return [line.strip() for line in sys.stdin]


def generate_triplets(source: str, adjacency_list) -> set[str]:
    destinations = adjacency_list[source]

    if len(destinations) < 2:
        return set()

    return {
        "-".join(sorted([source, dest1, dest2]))
        for dest1 in destinations
        for dest2 in destinations
        if dest1 != dest2
    }


def is_triple_valid(triple: str, adjacency_list) -> bool:
    first, second, third = triple.split("-")

    is_chiefs_computer_in_triple = (
        first.startswith("t") or second.startswith("t") or third.startswith("t")
    )
    are_computers_interconnected = (
        second in adjacency_list[first]
        and third in adjacency_list[first]
        and third in adjacency_list[second]
    )
    return is_chiefs_computer_in_triple and are_computers_interconnected


if __name__ == "__main__":
    lines = read_input()

    adjacency_list = defaultdict(set)
    for line in lines:
        source, destination = line.split("-")
        adjacency_list[source].add(destination)
        adjacency_list[destination].add(source)

    triples = [generate_triplets(source, adjacency_list) for source in adjacency_list]

    triples = reduce(lambda acc, item: acc | item, triples, set())
    triples = [triple for triple in triples if is_triple_valid(triple, adjacency_list)]
    triples = sorted(triples)

    print(len(triples))
