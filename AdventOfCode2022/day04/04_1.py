import sys


def read_input() -> list[str]:
    return [line for line in sys.stdin]


def is_pair_fully_contained(pair: list[str]) -> bool:
    first, second = pair

    first_start, first_end = [int(item) for item in first.split('-')]
    second_start, second_end = [int(item) for item in second.split('-')]

    first_inside_second = second_start <= first_start <= first_end <= second_end
    second_inside_first = first_start <= second_start <= second_end <= first_end

    return first_inside_second or second_inside_first

if __name__ == "__main__":
    inputs = [user_input.strip() for user_input in read_input()]
    pairs  = [input.split(',') for input in inputs]

    contained_pairs = [pair for pair in pairs if is_pair_fully_contained(pair)]

    print(len(contained_pairs))