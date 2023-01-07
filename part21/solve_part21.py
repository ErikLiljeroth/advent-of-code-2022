import copy
from typing import Tuple

def load_data(filename) -> Tuple[dict,dict]:
    with open(filename, 'r') as f:
        input = f.readlines()
    yell_dict, oper_dict = {}, {}
    for line in input:
        id, *job = line.replace(':', '').strip().split()
        if len(job) == 1:
            yell_dict[id] = eval(job[0])
        else:
            oper_dict[id] = job
    return yell_dict, oper_dict

def get_root_4_humn(humn_val, yell_dict, oper_dict) -> int:
    yell_dict_fcn = copy.deepcopy(yell_dict)
    yell_dict_fcn['humn'] = humn_val
    oper_dict_fcn = copy.deepcopy(oper_dict)
    while len(oper_dict_fcn) > 0:
        for key in oper_dict_fcn.keys():
            if oper_dict_fcn[key][0] in yell_dict_fcn.keys() and oper_dict_fcn[key][2] in yell_dict_fcn.keys():
                yell_dict_fcn[key] = round(eval(f'{yell_dict_fcn[oper_dict_fcn[key][0]]} {oper_dict_fcn[key][1]} {yell_dict_fcn[oper_dict_fcn[key][2]]}'))
                oper_dict_fcn.pop(key)
                break
    return yell_dict_fcn['root']

def binary_search(yell_dict, oper_dict, low, high) -> int:
    while low != high:
        mid = int((low + high)/2)
        nbor_left_result = abs(get_root_4_humn(mid-1, yell_dict, oper_dict))
        mid_result = abs(get_root_4_humn(mid, yell_dict, oper_dict))
        nbr_right_result = abs(get_root_4_humn(mid+1, yell_dict, oper_dict))
        if mid_result == 0:
            return mid
        elif nbr_right_result < mid_result:
            low = mid+1
        elif nbor_left_result < mid_result:
            high = mid-1
    return low

def main() -> None:
    # Part I
    yell_dict, oper_dict = load_data('input.txt')
    while len(oper_dict) > 0:
        for key in oper_dict.keys():
            if oper_dict[key][0] in yell_dict.keys() and oper_dict[key][2] in yell_dict.keys():
                yell_dict[key] = int(eval(f'{yell_dict[oper_dict[key][0]]} {oper_dict[key][1]} {yell_dict[oper_dict[key][2]]}'))
                oper_dict.pop(key)
                break
    print('Answer Part I:', yell_dict['root'])
    # Part II
    yell_dict, oper_dict = load_data('input.txt')
    oper_dict['root'][1] = '-'
    print('Answer Part II:', binary_search(yell_dict, oper_dict, low = 0, high = 2**48))

if __name__ == '__main__':
    main()