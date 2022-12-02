import sys

def read_input() -> list[str]:
    return [line for line in sys.stdin]

def determine_move(opponent_move: str, outcome: str) -> str:
    moves = {
        'A': {'X': 'S', 'Y': 'R', 'Z': 'P'},
        'B': {'X': 'R', 'Y': 'P', 'Z': 'S'},
        'C': {'X': 'P', 'Y': 'S', 'Z': 'R'},
    }

    return moves[opponent_move][outcome]

def calculate_score(round: list[str]) -> int:
    shape_score = {
        'R': 1, 
        'P': 2,
        'S': 3
    }

    result_score = {
        'X': 0,
        'Y': 3,
        'Z': 6
    }

    move = determine_move(round[0], round[1])
    return shape_score[move] + result_score[round[1]]


if __name__ == "__main__":
    inputs = [user_input.strip().split() for user_input in read_input()]
    scores = [calculate_score(round) for round in inputs]

    print(sum(scores))
