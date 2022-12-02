import sys

def read_input() -> list[str]:
    return [line for line in sys.stdin]

def determine_result(first: str, second: str) -> int:
    results = {
        'AX': 3,
        'AY': 6,
        'AZ': 0,

        'BX': 0,
        'BY': 3,
        'BZ': 6,
        
        'CX': 6,
        'CY': 0,
        'CZ': 3,
    }
    
    return results[first+second]

def calculate_score(round: list[str]) -> int:
    shape_score = {
        'X': 1, 
        'Y': 2,
        'Z': 3
    }
    return determine_result(round[0], round[1]) + shape_score[round[1]]


if __name__ == "__main__":
    inputs = [user_input.strip().split() for user_input in read_input()]
    scores = [calculate_score(round) for round in inputs]

    print(sum(scores))
