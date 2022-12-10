from typing import List

def check_left_trees(input_row, cur_col_idx: int) -> bool:
    conv_input_row = [int(val) for val in input_row]
    for left_idx in range(cur_col_idx):
        if conv_input_row[left_idx] >= conv_input_row[cur_col_idx]:
            return False
    return True

def check_right_trees(input_row, cur_col_idx: int) -> bool:
    conv_input_row = [int(val) for val in input_row]
    for right_idx in range(cur_col_idx+1, len(input_row)):
        if conv_input_row[right_idx] >= conv_input_row[cur_col_idx]:
            return False
    return True

def check_top_trees(input_col, cur_row_idx:int) -> bool:
    conv_input_col = [int(val) for val in input_col]
    for top_idx in range(cur_row_idx):
        if conv_input_col[top_idx] >= conv_input_col[cur_row_idx]:
            return False
    return True

def check_bottom_trees(input_col, cur_row_idx:int) -> bool:
    conv_input_col = [int(val) for val in input_col]
    for bottom_idx in range(cur_row_idx+1, len(input_col)):
        if conv_input_col[bottom_idx] >= conv_input_col[cur_row_idx]:
            return False
    return True

def left_score(input_row, cur_col_idx: int) -> int:
    conv_input_row = [int(val) for val in input_row]
    search_range = list(range(cur_col_idx))
    search_range.reverse()
    score = 0
    for left_idx in search_range:
        if conv_input_row[left_idx] < conv_input_row[cur_col_idx]:
            score += 1
        else:
            score+=1
            break
    return score

def right_score(input_row, cur_col_idx: int) -> int:
    conv_input_row = [int(val) for val in input_row]
    search_range = list(range(cur_col_idx+1, len(input_row))) # Note: not reversed
    score = 0
    for right_idx in search_range:
        if conv_input_row[right_idx] < conv_input_row[cur_col_idx]:
            score += 1
        else:
            score+=1
            break
    return score

def top_score(input_col, cur_row_idx:int) -> int:
    conv_input_col = [int(val) for val in input_col]
    search_range = list(range(cur_row_idx))
    search_range.reverse()
    score = 0

    for top_idx in search_range:
        if conv_input_col[top_idx] < conv_input_col[cur_row_idx]:
            score +=1
        else:
            score +=1
            break
    return score

def bottom_score(input_col, cur_row_idx:int) -> int:
    conv_input_col = [int(val) for val in input_col]
    search_range = list(range(cur_row_idx+1, len(input_col)))
    score = 0

    for bottom_idx in search_range:
        if conv_input_col[bottom_idx] < conv_input_col[cur_row_idx]:
            score += 1
        else:
            score+=1
            break
    return score

def main():
    filename = 'input.txt'

    # Part I
    with open(filename, "r") as f:
        input = f.readlines()
    visible_counter = 0
    input = [row.strip() for row in input]
    row_len = len(input[0])
    col_len = len(input)
    col_input = list(zip(*input))

    tree_counter = 0

    for row_idx in range(1,row_len-1):
        for col_idx in range(1, col_len-1):
            cur_tree = input[row_idx][col_idx]

            if check_left_trees(input[row_idx], col_idx):
                visible_counter += 1
            elif check_right_trees(input[row_idx], col_idx):
                visible_counter += 1
            elif check_top_trees(col_input[col_idx], row_idx):
                visible_counter += 1
            elif check_bottom_trees(col_input[col_idx], row_idx):
                visible_counter += 1
            tree_counter += 1

    # edge cases
    visible_counter += 2 * row_len
    visible_counter += 2* col_len - 4
    print('Answer part I:', visible_counter)

    # Part II

    input = [row.strip() for row in input]
    row_len = len(input[0])
    col_len = len(input)
    col_input = list(zip(*input))

    max_score = 0

    for row_idx in range(1,row_len-1):
        for col_idx in range(1, col_len-1):
            cur_tree = input[row_idx][col_idx]
            cur_tree_score = left_score(input[row_idx], col_idx) * right_score(input[row_idx], col_idx) * top_score(col_input[col_idx], row_idx) * bottom_score(col_input[col_idx], row_idx)
            if cur_tree_score > max_score:
                max_score = cur_tree_score

    print('Answer part II:', max_score)

if __name__ == '__main__':
    main()