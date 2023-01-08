from typing import List, Tuple

class HeightMap():

    def __init__(self, filename):
        with open(filename,'r') as f:
            input = f.readlines()
        self.matrix = []
        for idx,line in enumerate(input):
            stripped_line = line.strip()
            self.matrix.append(stripped_line)
            if 'S' in stripped_line:
                self.start_pos = (idx, stripped_line.index('S'))
            if 'E' in stripped_line:
                self.end_pos = (idx, stripped_line.index('E'))

        self.height_map = [[0 for _ in range(len(self.matrix[0]))] for _ in range(len(self.matrix))]
        self.possible_start_pos = set()
        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[row])):
                if self.matrix[row][col] == 'S':
                    self.height_map[row][col] = 1
                elif self.matrix[row][col] == 'E':
                    self.height_map[row][col] = ord('z')-ord('a') + 1
                else:
                    self.height_map[row][col] = ord(self.matrix[row][col]) - ord('a') + 1
                if self.height_map[row][col] == 1:
                    self.possible_start_pos.add((row,col))

    def get_val_at_pos(self, pos) -> int:
        row = pos[0]
        col = pos[1]
        return self.height_map[row][col]

    def is_valid(self, pos) -> bool:
        nbr_rows = len(self.height_map)
        nbr_cols = len(self.height_map[0])
        return pos[0] >= 0 and pos[0] < nbr_rows and pos[1] >= 0 and pos[1] < nbr_cols

def bfs(height_map, start_pos, end_pos) -> List[Tuple[int]]:
    alts = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    que = [[start_pos]]
    seen = set(start_pos)
    cnt = 0

    while que:
        cur_path = que.pop(0)
        cur_pos = cur_path[-1]
        cur_val = height_map.get_val_at_pos(cur_pos)
        if cur_val == 26 and cur_pos == end_pos:
            return cur_path
        for alt in alts:
            new_pos = (cur_pos[0] + alt[0], cur_pos[1] + alt[1])
            if height_map.is_valid(new_pos) and new_pos not in seen and height_map.get_val_at_pos(new_pos) <= (cur_val + 1):
                que.append(cur_path + [new_pos])
                seen.add(new_pos)
        cnt += 1
    return None

def main() -> None:
    # Part I
    height_map = HeightMap('input.txt')
    p = bfs(height_map, height_map.start_pos, height_map.end_pos)
    print('Answer Part I:', len(p)-1) # Remove one from length of path, since first pos does not count

    # Part II
    height_map = HeightMap('input.txt')
    path_lenghts = []
    for pos in height_map.possible_start_pos:
        try_path = bfs(height_map, pos, height_map.end_pos)
        if try_path is not None:
            path_lenghts.append(len(try_path)-1)
    print('Answer Part II:', min(path_lenghts))

if __name__ == '__main__':
    main()