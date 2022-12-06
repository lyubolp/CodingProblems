import sys


def read_input():
    return [line for line in sys.stdin]

def is_substr_unique(substr: str) -> bool:
    return len(set(substr)) == len(substr)

def find_marker(line: str) -> int:
    for i in range(len(line)):
        if is_substr_unique(line[i:i+14]):
            return i + 14

if __name__ == "__main__":
    inputs = [user_input.strip() for user_input in read_input()]

    print(find_marker(inputs[0]))
