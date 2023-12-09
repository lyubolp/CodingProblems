"""
A short script to set me up for [Advent of Code](https://adventofcode.com/)
"""
import os
import shutil
from datetime import datetime


if __name__ == "__main__":
    current_day = datetime.today().strftime('%d')
    current_year = datetime.today().strftime('%Y')

    current_day_directory_path = os.path.join(f'AdventOfCode{current_year}', f'day{current_day}')

    # Create the directory
    os.makedirs(current_day_directory_path, exist_ok=True)

    # Create the files with the initial code
    # TODO - Add support for different languages than Python
    part_1_solution_path = os.path.join(current_day_directory_path, f'{current_day}_1.py')
    part_2_solution_path = os.path.join(current_day_directory_path, f'{current_day}_2.py')

    # Copy the sample code
    aoc_sample_code_path = os.path.join('utils', 'aoc_sample.py')
    shutil.copy2(aoc_sample_code_path, part_1_solution_path)
    shutil.copy2(aoc_sample_code_path, part_2_solution_path)

    # Create the empty input files
    input_small_path = os.path.join(current_day_directory_path, 'input_small.txt')
    input_large_path = os.path.join(current_day_directory_path, 'input_large.txt')

    open(input_small_path, 'w').close()
    open(input_large_path, 'w').close()
