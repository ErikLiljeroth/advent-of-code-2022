from typing import List

class CRT:

    def __init__(self) -> None:
        self.matrix = [['.'] * 40 for i in range(6)]

    def draw_pixel(self, cycle:int, sprite_X:int) -> None:
        crt_row = int((cycle-1)/40)
        crt_col = (cycle-1) % 40
        if abs(crt_col-sprite_X) <= 1:
            self.matrix[crt_row][crt_col] = '#'
        else:
            pass

    def print(self, to_terminal = True) -> List[List[str]]:
        if to_terminal:
            for pixel_row in self.matrix:
                print(pixel_row)
        return self.matrix


class CPU:

    def __init__(self, interesting_cycles: List[int]) -> None:
        self.X = 1
        self.cycle = 0
        self.interesting_cycles = interesting_cycles
        self.interesting_signal_strengths = []
        self.CRT = CRT()

    def _check_interesting_signal_strength(self) -> None:
        if self.cycle in self.interesting_cycles:
            self.interesting_signal_strengths.append(self.X * self.cycle)

    def noop(self) -> None:
        self.cycle += 1
        self._check_interesting_signal_strength()
        self.CRT.draw_pixel(cycle=self.cycle, sprite_X=self.X)

    def addx(self, val: int) -> None:
        self.cycle += 1
        self._check_interesting_signal_strength()
        self.CRT.draw_pixel(cycle=self.cycle, sprite_X=self.X)
        self.cycle += 1
        self._check_interesting_signal_strength()
        self.CRT.draw_pixel(cycle=self.cycle, sprite_X=self.X)
        self.X += val

    def check_experiment_done(self) -> int:
        if len(self.interesting_signal_strengths) == len(self.interesting_cycles):
            return sum(self.interesting_signal_strengths)
        else:
            return None

def main():
    filename = 'input.txt'

    with open(filename, "r") as f:
        input = f.readlines()

    # Solve part I & II
    cpu = CPU(interesting_cycles=[20, 60, 100, 140, 180, 220])

    for line in input:
        inst, *val = line.strip().split()
        val = int(val[0]) if val else None
        if inst == 'addx':
            cpu.addx(val)
        elif inst == 'noop':
            cpu.noop()
        else:
            print(f'instruction {inst} not recognized')

        if cpu.cycle > 240:
            break

    print('Answer part I:', cpu.check_experiment_done())

    screen = cpu.CRT.print(to_terminal = False)

    print('Answer part II:', 'check output.txt -> "RGZEHURK"')
    with open('output.txt', 'w+') as f:
        for row in screen:
            for char in row:
                f.write(char)
            f.write('\n')

if __name__ == '__main__':
    main()