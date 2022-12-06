from typing import List

def find_idx_of_n_unique_chars(input:str, n=4) -> int:
    input_len = len(input)
    for i in range(input_len-n):
        str_slice = input[i:i+n]
        if len(set(str_slice)) == n:
            return i+n
    return None

def main() -> None:
    filename = 'input.txt'
    with open(filename, "r") as f:
        input = f.read()
    print('solve part I:', find_idx_of_n_unique_chars(input, 4))
    print('solve part II:', find_idx_of_n_unique_chars(input, 14))

if __name__=='__main__':
    main()