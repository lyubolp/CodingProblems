import os
import sys

from typing import Dict, List, Tuple

CD_DIR = '$ cd'
LS_DIR = '$ ls'

def read_input() -> List[str]:
    return [line for line in sys.stdin]


def split_input(inputs: List[str]) -> Tuple[Dict[str, List[Tuple[str, int]]], List[str]]:
    dir_data = {}
    dirs = {'/'}

    current_dir = ''
    is_ls_active = False
    for line in inputs:
        if line.startswith(CD_DIR):
            arg = line.split()[2]
            if arg == '..':
                current_dir = os.path.split(current_dir)[0]
            elif arg == '/':
                current_dir = '/'
            else:
                current_dir = os.path.join(current_dir, arg)

            is_ls_active = False
        elif line.startswith(LS_DIR):
            is_ls_active = True
        elif is_ls_active:
            size, name = line.split()
            if size == 'dir':
                size = 0
            else:
                size = int(size)

            dirs.add(current_dir)
            if current_dir in dir_data:
                dir_data[current_dir].append((name, size))
            else:                
                dir_data[current_dir] = [(name, size)]
        else:
            pass

    return dir_data, dirs

def calculate_dir_size(dir_data: Dict[str, List[Tuple[str, int]]], dir_name: str) -> int:
    result = 0

    stack = [dir_name]

    while len(stack) > 0:
        current_dir = stack.pop()

        for item, size in dir_data[current_dir]:
            if size == 0:
                stack.append(os.path.join(current_dir, item))
            else:
                result += size
    
    return result

if __name__ == "__main__":
    inputs = [user_input.strip() for user_input in read_input()]
    dir_data, dirs = split_input(inputs)

    dirs_with_sizes = {dir: calculate_dir_size(dir_data, dir) for dir in dirs}

    max_space = 70000000
    
    used_space = dirs_with_sizes['/']
    free_space = max_space - used_space

    target_free_space = 30000000
    space_to_free_up = target_free_space - free_space

    candidates_to_delete = [(dir, size) for dir, size in dirs_with_sizes.items() if size >= space_to_free_up]
    candidates_to_delete = sorted(candidates_to_delete, key=lambda x: x[1])

    # print(candidates_to_delete)
    print(candidates_to_delete[0][1])

