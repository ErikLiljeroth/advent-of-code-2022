import re

def interval_contains_other(line_str:str) -> bool:
    splt_nbrs = re.split(r'[-,]', line_str.strip())

    # if second interval contains first
    if int(splt_nbrs[0]) >= int(splt_nbrs[2]) and int(splt_nbrs[1]) <= int(splt_nbrs[3]):
        return True
    # if first interval contains second
    elif int(splt_nbrs[2]) >= int(splt_nbrs[0]) and int(splt_nbrs[3]) <= int(splt_nbrs[1]):
        return True
    # otherwise no contains
    else:
        return False

def intervals_overlap(line_str:str) -> bool:
    splt_nbrs = re.split(r'[-,]', line_str.strip())

    # if first interval shifted left
    if int(splt_nbrs[0]) <= int(splt_nbrs[2]) and int(splt_nbrs[1]) >= int(splt_nbrs[2]):
        return True
    # if first interval shifted right
    elif int(splt_nbrs[0]) <= int(splt_nbrs[3]) and int(splt_nbrs[1]) >= int(splt_nbrs[3]):
        return True
    # if any interval contains the other
    elif interval_contains_other(line_str):
        return True
    else:
        return False

def intervals_contains_other_with_set(line_str:str) -> bool:
    splt_nbrs = re.split(r'[-,]', line_str.strip())
    s1 = set(range(int(splt_nbrs[0]), int(splt_nbrs[1])+1))
    s2 = set(range(int(splt_nbrs[2]), int(splt_nbrs[3])+1))
    return len(s1.intersection(s2)) in [len(s1), len(s2)]

def intervals_overlap_with_set(line_str:str) -> bool:
    splt_nbrs = re.split(r'[-,]', line_str.strip())
    s1 = set(range(int(splt_nbrs[0]), int(splt_nbrs[1])+1))
    s2 = set(range(int(splt_nbrs[2]), int(splt_nbrs[3])+1))
    return len(s1.intersection(s2)) > 0

def solve_part_I(input):
    counter = 0
    for row in input:
        if intervals_contains_other_with_set(row):
            counter += 1
    return counter

def solve_part_II(input):
    counter = 0
    for row in input:
        if intervals_overlap_with_set(row):
            counter += 1
    return counter

def main():
    filename = 'input.txt'

    with open(filename, 'r') as f:
        input = f.readlines()

    print('Answer part I:', solve_part_I(input))
    print('Answer part II:', solve_part_II(input))

if __name__ == '__main__':
    main()