from typing import List, Tuple

class Map:

    def _coord_between_points(self, p_a, p_b):
        if p_a[0] == p_b[0]:
            interim_points = [(p_a[0],p + min(p_b[1], p_a[1])) for p in range(abs(p_b[1]-p_a[1]) + 1)]
        elif p_a[1] == p_b[1]:
            interim_points = [(p + min(p_b[0], p_a[0]), p_b[1]) for p in range(abs(p_b[0]-p_a[0]) + 1)]
        else:
            print('cannot create diagonal path')
            return None
        return interim_points

    def _draw_rocks(self, points):
        for p in points:
            self.matrix[p[0]][p[1]-min(self.y_set)] = '#'

    def __init__(self, input, sand_pouring_pos: tuple, part = 'a') -> None:
        self.x_set = set()
        self.y_set = set()
        self.buffer = 0 # extra map outside paths
        self.sand_pouring_pos = sand_pouring_pos
        self.sand_counter = 0
        # build map based on input
        for path in input:
            for point in path:
                self.x_set.add(point[0])
                self.y_set.add(point[1])
        if part == 'a':
            self.matrix = [['.'] * (max(self.y_set) - min(self.y_set) + 1) for _ in range(max(self.x_set) + 1)]
        else:
            # y set - increase map
            self.y_set.update(list(range(min(self.y_set)-400, min(self.y_set)+1)))
            self.y_set.update(list(range(max(self.y_set)-1, max(self.y_set)+400)))
            # x set add bottom
            self.x_set.add(max(self.x_set)+1)
            self.x_set.add(max(self.x_set)+1)

            self.matrix = [['.'] * (max(self.y_set) - min(self.y_set) + 1) for _ in range(max(self.x_set) + 1)]
            # build floor
            for i in range(len(self.matrix[0])):
                self.matrix[-1][i] = '#'

        # Draw rock paths
        for line in input:
            for idx,point in enumerate(line):
                if idx == 0:
                    continue
                rock_points = self._coord_between_points(line[idx-1], line[idx])
                self._draw_rocks(rock_points)

        # Draw sand pouing pos
        self.matrix[self.sand_pouring_pos[0]][self.sand_pouring_pos[1] - min(self.y_set)] = '+'

    def print(self):
        for x_row in self.matrix:
            for char in x_row:
                print(char,end='')
            print()

    def add_and_move_sand(self, init_pos) -> bool:
        # return True if sand stopped, ow False if sand goes outisde map
        cur_pos = list(init_pos)
        for i in range(max(self.x_set)):
            below_row = self.matrix[cur_pos[0] + 1][cur_pos[1]-min(self.y_set)-1:cur_pos[1]-min(self.y_set)+2]
            if not below_row:
                return False
            elif below_row[1] not in ['#', 'o']:
                cur_pos[0] += 1
            elif below_row[0] not in ['#', 'o']:
                cur_pos[0] += 1
                cur_pos[1] -= 1
            elif below_row[2] not in ['#', 'o']:
                cur_pos[0] += 1
                cur_pos[1] += 1
            else:
                if self.matrix[cur_pos[0]][cur_pos[1] - min(self.y_set)] != 'o':
                    self.sand_counter += 1
                    self.matrix[cur_pos[0]][cur_pos[1] - min(self.y_set)] = 'o'
                    return True
                return False
        return False

def main():
    filename = 'input.txt'
    with open(filename, 'r') as f:
        input_not_parsed = f.readlines()
    input = []
    for line in input_not_parsed:
        parsed_line = [eval(s) for s in line.strip().split(' -> ')]
        parsed_line = [(p[1], p[0]) for p in parsed_line]
        input.append(parsed_line)

    # Part I
    map = Map(input, sand_pouring_pos=(0,500), part='a')
    flag = True
    cnt = 0
    while flag:
        flag = map.add_and_move_sand((0,500))
        if cnt % 10000 == 0:
            print(cnt)
        cnt += 1
    print('Answer Part I:', map.sand_counter)

    # Part II
    map = Map(input, sand_pouring_pos=(0,500), part='b')
    flag = True
    cnt = 0
    while flag:
        flag = map.add_and_move_sand((0,500))
        if cnt % 1000 == 0:
            print('Created',cnt, 'sand so far...')
        cnt += 1
    print('Done!')
    print()
    print('Answer Part II:', map.sand_counter)

if __name__ == '__main__':
    main()