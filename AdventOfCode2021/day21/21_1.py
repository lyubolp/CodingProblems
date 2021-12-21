#!/usr/bin/python3

import sys
from typing import List, Tuple


def read_input() -> List[str]:
    return [line.strip() for line in sys.stdin if line != '\n']


def get_starting_position(line: str) -> int:
    return int(line.split(':')[1].strip())


def move(player_position: int, dice: int) -> int:
    player_position += dice
    if player_position > 10:
        player_position %= 10
        if player_position == 0:
            player_position = 10

    return player_position


def roll_dice(current_dice: int) -> int:
    current_dice += 1

    if current_dice > 100:
        current_dice = 1

    return current_dice


if __name__ == "__main__":
    lines = read_input()

    player_1_position = get_starting_position(lines[0])
    player_2_position = get_starting_position(lines[1])

    dice = 1
    times_dice_rolled = 0

    players = [(player_1_position, 0), (player_2_position, 0)]

    while players[0][1] < 1000 and players[1][1] < 1000:
        for i, (player_pos, player_score) in enumerate(players):
            # print(f"Player {i + 1}: pos - {player_pos}, score - {player_score}")
            # print(f"Dice: {dice}")

            to_move = 0
            for roll in range(3):
                to_move += dice
                dice = roll_dice(dice)
                times_dice_rolled += 1

            player_pos = move(player_pos, to_move)
            player_score += player_pos
            players[i] = (player_pos, player_score)
            # print(f"Player {i + 1}: pos - {player_pos}, score - {player_score}")

            if player_score >= 1000:
                break

    print(min(players[0][1], players[1][1]) * times_dice_rolled)
