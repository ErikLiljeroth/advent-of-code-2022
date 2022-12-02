from typing import List

# Rock, paper, scissors - part I
OUTCOME_POINTS = {
    'A X': 3 + 1,
    'A Y': 6 + 2,
    'A Z': 0 + 3,
    'B X': 0 + 1,
    'B Y': 3 + 2,
    'B Z': 6 + 3,
    'C X': 6 + 1,
    'C Y': 0 + 2,
    'C Z': 3 + 3
}

# counter action dict - part II
# X: lose, Y:draw, Z:win
OUTCOME_ACTION = {
    'A X': 'A Z',
    'A Y': 'A X',
    'A Z': 'A Y',
    'B X': 'B X',
    'B Y': 'B Y',
    'B Z': 'B Z',
    'C X': 'C Y',
    'C Y': 'C Z',
    'C Z': 'C X'
}

# part I & II
def calc_points(input: List[str]) -> int:
    total_points = 0
    for row in input:
        cur_row = row.strip()
        total_points += OUTCOME_POINTS[cur_row]

    return total_points

# part II
def transform_action_calc_points(input: List[str]) -> int:
    total_points = 0
    for row in input:
        cur_row = row.strip()
        total_points += OUTCOME_POINTS[OUTCOME_ACTION[cur_row]]
    return total_points

def main() -> None:

    filename = 'input.txt'

    with open(filename, 'r') as f:
        input = f.readlines()

    # solve part I
    print('part I:', calc_points(input))

    #solve part II
    print('part II',transform_action_calc_points(input))

if __name__ == '__main__':
    main()
