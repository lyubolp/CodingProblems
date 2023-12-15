import sys
from functools import reduce


def read_input() -> list[str]:
    return [line.strip() for line in sys.stdin]


def hash_algorithm(sequence: str) -> int:
    return reduce(hash_algorithm_character, sequence, 0)


def hash_algorithm_character(start_value: int, character: str) -> int:
    return ((start_value + ord(character)) * 17) % 256


if __name__ == "__main__":
    lines = read_input()
    sequences = lines[0].split(',')

    hashed_sequences = [hash_algorithm(sequence) for sequence in sequences]

    result = sum(hashed_sequences)
    print(result)
