import sys
from functools import reduce


def read_input() -> list[str]:
    return [line.strip() for line in sys.stdin]


def generate_next_sequence(sequence: list[int]) -> list[int]:
    sequence_offset = zip(sequence, sequence[1:])

    return [second - first for first, second in sequence_offset]


def is_sequence_all_zeros(sequence: list[int]) -> bool:
    return set(sequence) == set([0])


def extrapolate_sequences(sequences: list[list[int]]) -> int:
    return reduce(lambda acc, seq: acc + seq[-1], reversed(sequences), 0)


if __name__ == "__main__":
    lines = read_input()

    history_sequences = [[int(value) for value in line.split()] for line in lines]

    results = []
    for sequence in history_sequences:
        current_sequnce = sequence
        sequences = [current_sequnce]
        while not is_sequence_all_zeros(current_sequnce):
            current_sequnce = generate_next_sequence(current_sequnce)
            sequences.append(current_sequnce)

        results.append(extrapolate_sequences(sequences))

    result = sum(results)
    print(result)
