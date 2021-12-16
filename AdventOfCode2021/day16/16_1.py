#!/usr/bin/python3
import sys
from typing import List, Tuple, Dict, Set
from queue import PriorityQueue


def read_input() -> List[str]:
    return [line.strip() for line in sys.stdin if line != '\n']


def hex_packet_to_binary(hex_num: str) -> str:
    hex_map = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111'
    }

    return "".join([hex_map[c] for c in hex_num])


def get_packet_version(packet) -> int:
    return int(packet[:3], base=2)


def get_packet_type_id(packet) -> int:
    return int(packet[3:6], base=2)


def calculate_versions(packet: str) -> int:
    result = 0

    while len(packet) >= 7:
        if '1' not in packet:
            break

        current_packet_version = get_packet_version(packet)
        current_packet_type_id = get_packet_type_id(packet)
        result += current_packet_version

        print(f"packet={packet}, "
              f"current_packet_version={current_packet_version}, "
              f"current_packet_type_id={current_packet_type_id}")

        packet = packet[6:]

        if current_packet_type_id == 4:
            while packet[0] != '0':
                packet = packet[5:]
            packet = packet[5:]
        else:
            length_type_id = packet[0]
            if length_type_id == '0':
                packet = packet[16:]

            elif length_type_id == '1':
                packet = packet[12:]
            else:
                raise ValueError("Invalid parsing")

    return result


if __name__ == "__main__":
    hex_packet = read_input()[0]
    packet = hex_packet_to_binary(hex_packet)
    print(calculate_versions(packet))
