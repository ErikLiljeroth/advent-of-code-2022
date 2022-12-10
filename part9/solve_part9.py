from typing import List, Tuple

class Knot():

    def __init__(self) -> None:
        self.x = 0
        self.y = 0

    def move_knot(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def chain_move_knot(self, lead_x:int, lead_y:int):
        x_diff = lead_x - self.x
        y_diff = lead_y - self.y
        if abs(x_diff) == 2 and abs(y_diff) == 2:
            if x_diff > 0 and y_diff > 0:
                self.x = lead_x - 1
                self.y = lead_y - 1
            elif x_diff > 0 and y_diff < 0:
                self.x = lead_x - 1
                self.y = lead_y + 1
            elif x_diff < 0 and y_diff > 0:
                self.x = lead_x + 1
                self.y = lead_y - 1
            else:
                self.x = lead_x + 1
                self.y = lead_y + 1

        elif abs(x_diff) == 2:
            self.x = self.x + 1 if x_diff > 0 else self.x - 1
            if self.y != lead_y:
                self.y = lead_y
        elif abs(y_diff) == 2:
            self.y = self.y + 1 if y_diff > 0 else self.y - 1
            if self.x != lead_x:
                self.x = lead_x
        else:
            return

    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y

class KnotTrainSimulation():

    def __init__(self, nbr_knots) -> None:
        self.train = []
        for i in range(nbr_knots):
            self.train.append(Knot())
        self.t_positions = []
        self.t_positions.append((self.train[-1].x, self.train[-1].y))

    def _find_initial_step(self, dir) -> Tuple[int]:
        output_x = self.train[0].get_x()
        output_y = self.train[0].get_y()
        if dir == 'R':
            output_x += 1
        elif dir == 'L':
            output_x -= 1
        elif dir == 'U':
            output_y += 1
        else:
            output_y -= 1
        return (output_x, output_y)


    def iterate(self, dir):
        new_x, new_y = self._find_initial_step(dir)
        self.train[0].move_knot(new_x, new_y)
        prev_x, prev_y = new_x, new_y
        for idx, knot in enumerate(self.train):
            if idx == 0:
                pass
            else:
                knot.chain_move_knot(prev_x, prev_y)
                prev_x = knot.x
                prev_y = knot.y
                if idx == len(self.train) - 1:
                    if (knot.x, knot.y) not in self.t_positions:
                        self.t_positions.append((knot.x, knot.y))

def main():
    filename = 'input.txt'

    with open(filename, "r") as f:
        input = f.readlines()

    # Part 1
    sim_part1 = KnotTrainSimulation(nbr_knots=2)

    for line in input:
        dir, nbr_steps = line.strip().split()
        nbr_steps = int(nbr_steps)
        for i in range(nbr_steps):
            sim_part1.iterate(dir)
    print('Answer part I:', len(sim_part1.t_positions))

    # Part II
    sim_part2 = KnotTrainSimulation(nbr_knots=10)

    for line in input:
        dir, nbr_steps = line.strip().split()
        nbr_steps = int(nbr_steps)
        for i in range(nbr_steps):
            sim_part2.iterate(dir)
    print('Answer part II:', len(sim_part2.t_positions))

if __name__ == '__main__':
    main()