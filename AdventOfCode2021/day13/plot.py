#!/usr/bin/python3
from typing import List

# Was too lazy to plot stuff in Haskell, so I've made the plotting of the points in Python

def print_line(coordinates: List[int]) -> str:
    return "".join(["█" if i in coordinates else " " for i in range(max(coordinates)+1)])

if __name__ == "__main__":
    # Paste the output of 13_2.hs here
    points = [
        [0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [1, 2], [2, 2], [3, 0], [3, 1], [3, 2], [3, 3], 
        [3, 4], [3, 5], [5, 0], [5, 4], [5, 5], [6, 0], [6, 3], [6, 5], [7, 0], [7, 2], [7, 5], [8, 0], 
        [8, 1], [8, 5], [10, 0], [10, 1], [10, 2], [10, 3], [10, 4], [10, 5], [11, 5], [12, 5], [13, 5], 
        [15, 0], [15, 1], [15, 2], [15, 3], [15, 4], [15, 5], [16, 0], [16, 2], [16, 5], [17, 0], [17, 2], 
        [17, 5], [18, 0], [18, 5], [20, 0], [20, 1], [20, 2], [20, 3], [20, 4], [20, 5], [21, 2], [22, 2], 
        [23, 0], [23, 1], [23, 2], [23, 3], [23, 4], [23, 5], [25, 4], [26, 5], [27, 0], [27, 5], [28, 0], 
        [28, 1], [28, 2], [28, 3], [28, 4], [30, 0], [30, 1], [30, 2], [30, 3], [30, 4], [30, 5], [31, 0], 
        [31, 3], [32, 0], [32, 3], [32, 4], [33, 1], [33, 2], [33, 5], [35, 0], [35, 1], [35, 2], [35, 3], 
        [35, 4], [35, 5], [36, 2], [37, 1], [37, 3], [37, 4], [38, 0], [38, 5]]
    
    max_lines = max([p[1] for p in points])

    result = []
    for i in range(max_lines+1):
        result.append(print_line([p[0] for p in points if p[1] == i]))

    print("\n".join(result))