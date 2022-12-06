from typing import List, Tuple
import copy

def parse_input(input:List[str]) -> Tuple[List[List[str]], List[int], List[List[int]]]:
    crate_rows = []
    crate_nbrs = []
    instrc = []
    for row in input:
        if row.startswith('move'):
            z = row.replace('move ', '').replace('from ', '').replace('to ', '').strip()
            z = z.split(' ')
            z = [int(x) for x in z]
            instrc.append(z)
        elif row.startswith(' 1'):
            x = row.strip().replace('  ', '')
            x = x.split(' ')
            crate_nbrs = [int(c) for c in x]
        elif row.startswith('\n'):
            pass
        else:
            x = row.replace('    ', ' ')
            x = x.split(' ')
            x = [r.strip('\n') for r in x]
            crate_rows.append(x)

    return crate_rows, crate_nbrs, instrc

def create_stacks(crate_nbrs:List[int], crate_rows:List[List[str]]) -> List[List[str]]:
    stacks = {}
    for nbr in crate_nbrs:
        cur_stack = []
        for crate_row in crate_rows:
            if crate_row[nbr-1] != '':
                cur_stack.append(crate_row[nbr-1])
        stacks[nbr] = cur_stack
        stacks[nbr].reverse()

    return stacks

def find_top_crates(stacks:List[List[str]]) -> str:
    crates_str = ''
    for key in stacks.keys():
        crates_str = crates_str + stacks[key].pop().strip('[').strip(']')
    return crates_str

def solve_part_I(input: List[str]) -> str:
    crate_rows, crate_nbrs, instrc = parse_input(input)
    stacks = create_stacks(crate_nbrs, crate_rows)

    stacks_adj = copy.copy(stacks)

    for ins in instrc:
        for t in range(ins[0]):
            elem = stacks_adj[ins[1]].pop()
            stacks_adj[ins[2]].append(elem)

    return find_top_crates(stacks_adj)

def solve_part_II(input: List[str]) -> str:
    crate_rows, crate_nbrs, instrc = parse_input(input)
    stacks = create_stacks(crate_nbrs, crate_rows)

    stacks_adj = copy.copy(stacks)

    for ins in instrc:
        if ins[0] == 1:
            elem = stacks_adj[ins[1]].pop()
            stacks_adj[ins[2]].append(elem)

        if ins[0] > 1:
            crate_set = []
            for t in range(ins[0]):
                crate_set.append(stacks_adj[ins[1]].pop())
            crate_set.reverse()
            stacks_adj[ins[2]].extend(crate_set)
        else:
            pass
    return find_top_crates(stacks_adj)


def main():
    filename = 'input.txt'

    with open(filename, 'r') as f:
        input = f.readlines()

    print('solve part I:', solve_part_I(input))
    print('solve part II:', solve_part_II(input))

if __name__ == '__main__':
    main()