from typing import List
import os

def parse_input(input:List[str]):
    dirs = {}
    sub_dirs = {}
    for row in input:
        if row[0] == '$':
            _, cmd, *args = row.split()
            if cmd == 'cd':
                path = args[0]
                if path == '/':
                    cur_dir = path
                else:
                    cur_dir = os.path.normpath(os.path.join(cur_dir, path))
                if cur_dir not in dirs:
                    dirs[cur_dir] = 0
                    sub_dirs[cur_dir] = []
        else:
            size, fname = row.split()
            if size == 'dir':
                sub_dirs[cur_dir].append(os.path.normpath(os.path.join(cur_dir, fname)))
            else:
                dirs[cur_dir] += int(size)
    return dirs, sub_dirs

def get_dir_size(dir_name:str, dirs:dict, sub_dirs:dict) -> int:
    """Recursive function with base case if sub_dirs points to empty list for any key

    Args:
        dir_name (str): name of directory to compute size for
        dirs (dict): dictionary over directories
        sub_dirs (dict): dictionary over sub directories

    Returns:
        int: directory size including files and sub directories (and files)
    """
    dir_size = dirs[dir_name]
    for d in sub_dirs[dir_name]:
        if d in dirs:
            dir_size += get_dir_size(d, dirs, sub_dirs)
    return dir_size

def main():
    filename = 'input.txt'

    with open(filename, "r") as f:
        input = f.readlines()

    # part 1
    dirs, sub_dirs = parse_input(input)
    totsize = 0
    for d in dirs:
        dsize = get_dir_size(d, dirs, sub_dirs)
        if dsize <= 100000:
            totsize += dsize
    print('Answer part I:', totsize)

    # Part II
    dirs, sub_dirs = parse_input(input)
    dir_sizes = []
    used_dir_space = get_dir_size('/', dirs, sub_dirs)
    unused_dir_space = 70000000 - used_dir_space
    required_disc_space = 30000000 - unused_dir_space
    for dir_name in dirs:
        dir_size = get_dir_size(dir_name, dirs, sub_dirs)
        if dir_size >= required_disc_space:
            dir_sizes.append(dir_size)
    dir_sizes.sort()
    print('Answer part II:', dir_sizes[0])


if __name__ == '__main__':
    main()