import string
from typing import List

def _count_chars(str:str) -> dict:
    count_dict = {}
    for char in str:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    return count_dict

def find_unique_char(str: str) -> str:
    len_str = len(str)
    pivot = int(len_str/2)

    first_part_str = str[:pivot]
    second_part_str = str[pivot:]

    char_count_dict = _count_chars(first_part_str)

    for char in second_part_str:
        if char in char_count_dict:
            return char
    return None

def find_common_item(group_str_list: List[str]) -> str:
    count_dict_1 = _count_chars(group_str_list[0])
    count_dict_2 = _count_chars(group_str_list[1])

    for char in group_str_list[2]:
        if char in count_dict_1 and char in count_dict_2:
            return char
    return None

def solve_part_I(input:List[str]) -> int:
    total_points = 0
    for row in input:
        total_points += string.ascii_letters.index(find_unique_char(row)) + 1
    return total_points

def solve_part_II(input:List[str]) -> int:
    total_points = 0
    for i in range(0, len(input), 3):
        common_char = find_common_item([input[i], input[i+1], input[i+2]])
        total_points += string.ascii_letters.index(common_char) + 1
    return total_points

def main() -> None:
    filename = 'input.txt'
    with open(filename, 'r') as f:
        input = f.readlines()

    print('Answer part I:', solve_part_I(input))
    print('Answer part II:', solve_part_II(input))

if __name__ == '__main__':
    main()