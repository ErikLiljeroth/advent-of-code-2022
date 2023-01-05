import copy

def solve(part, filename) -> int:
    dec_key = 811589153

    filename = filename
    with open(filename, 'r') as f:
        input = f.readlines()
    if part == 'I':
        iter = 1
        input = [eval(row) for row in input]
    else:
        iter = 10
        input = [eval(row) * dec_key for row in input]

    input_len = len(input)
    output_keys = list(range(input_len))
    output_vals = copy.copy(input)

    for i in range(iter):
        for idx, val in enumerate(input):
            cur_output_idx = output_keys.index(idx)
            new_output_idx = (cur_output_idx + val) % (input_len - 1)
            # according to example: nbr jumps to end of list if calculated idx according to formulae above is 0
            if new_output_idx == 0:
                new_output_idx = input_len-1

            output_keys.pop(cur_output_idx)
            output_keys.insert(new_output_idx, idx)
            output_vals.pop(cur_output_idx)
            output_vals.insert(new_output_idx, val)

    # Find score
    idx_val_0 = output_vals.index(0)
    score_idxs = [(1000 + idx_val_0) % input_len, (2000 + idx_val_0) % input_len, (3000 + idx_val_0) % input_len]
    scores = [output_vals[idx] for idx in score_idxs]
    return sum(scores)

def main():
    # Part I
    print('Answer Part I:', solve('I', 'input.txt'))
    print()
    # Part II
    print('Answer Part II:', solve('II', 'input.txt'))

if __name__ == '__main__':
    main()