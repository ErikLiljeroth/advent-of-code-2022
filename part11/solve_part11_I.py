from typing import List

class Monkey:

    def __init__(self, monkey_nbr:int, starting_items:List[int], operation:List[str], divisible:int, test_true_monkey:int, test_false_monkey:int) -> None:
        self.monkey_nbr = monkey_nbr
        self.items = starting_items
        self.operation = operation
        self.divisible = divisible
        self.test_true_monkey = test_true_monkey
        self.test_false_monkey = test_false_monkey
        self.nbr_inspected = 0

    def _update_worry_level(self, old_worry_level) -> int:
        if self.operation[0] == '+':
            if self.operation[1] != 'old':
                addend = int(self.operation[1])
                return old_worry_level + addend
            else:
                return old_worry_level + old_worry_level
        elif self.operation[0] == '*':
            if self.operation[1] != 'old':
                factor = int(self.operation[1])
                return old_worry_level * factor
            else:
                return old_worry_level * old_worry_level
        else:
            print('operation not recognized')
            return None

    def inspect_and_throw(self) -> dict:
        throw_items = {}
        throw_items[self.test_true_monkey] = []
        throw_items[self.test_false_monkey] = []
        #print('items',self.items)
        for item in self.items:
            self.nbr_inspected += 1
            new_worry_level = self._update_worry_level(item)
            bored_worry_level = int(new_worry_level/3)
            #bored_worry_level = new_worry_level
            if bored_worry_level % self.divisible == 0:
                throw_items[self.test_true_monkey].append(bored_worry_level)
            else:
                throw_items[self.test_false_monkey].append(bored_worry_level)
        self.items = []
        #print('throw items', throw_items)
        return throw_items

    def receive_item(self, worry_level):
        self.items.append(worry_level)

class MonkeySimulation:

    def __init__(self) -> None:
        self.monkeys = {}

    def add_monkey(self, monkey:Monkey):
        self.monkeys[monkey.monkey_nbr] = monkey

    def iterate_round(self):
        for monkey_nbr in self.monkeys:
            throw_items = self.monkeys[monkey_nbr].inspect_and_throw()
            #print(throw_items)
            for monkey_nbr in throw_items:
                for item in throw_items[monkey_nbr]:
                    self.monkeys[monkey_nbr].receive_item(item)

    def compute_monkey_business(self) -> int:
        inspections = []
        for monkey_nbr in self.monkeys:
            inspections.append(self.monkeys[monkey_nbr].nbr_inspected)
        inspections.sort()
        return inspections, inspections[-1] * inspections[-2]

    def print_monkey_items(self):
        for monkey_nbr in self.monkeys:
            print(self.monkeys[monkey_nbr].items)

def parse_monkey_lines(monkey_lines):
    for line in monkey_lines:
        stripped_line = line.strip()
        if stripped_line.startswith('Monkey'):
            monkey_nbr = int(stripped_line.strip(':').split()[1])
        elif stripped_line.startswith('Starting'):
            _, items = stripped_line.split(':')
            items = items.strip().split(', ')
            items = [int(i) for i in items]
        elif stripped_line.startswith('Operation'):
            _,_,_,_,*operation = stripped_line.split()
        elif stripped_line.startswith('Test'):
            _,_,_,divisor = stripped_line.split()
            divisor = int(divisor)
        elif stripped_line.startswith('If true'):
            _,_,_,_,_,next_monkey_true = stripped_line.split()
            next_monkey_true = int(next_monkey_true)
        elif stripped_line.startswith('If false'):
            _,_,_,_,_,next_monkey_false = stripped_line.split()
            next_monkey_false = int(next_monkey_false)
        else:
            'unknown input row'
    return monkey_nbr, items, operation, divisor, next_monkey_true, next_monkey_false

def parse_input(input) -> dict:
    monkeys = {}
    monkey_lines = []
    for idx,line in enumerate(input):
        if idx == len(input)-1:
            monkey_lines.append(line)
            monkey_nbr, items, operation, divisor, next_monkey_true, next_monkey_false = parse_monkey_lines(monkey_lines)
            monkeys[monkey_nbr] = [items, operation, divisor, next_monkey_true, next_monkey_false]
        elif line != '\n':
            monkey_lines.append(line)
        else:
            monkey_nbr, items, operation, divisor, next_monkey_true, next_monkey_false = parse_monkey_lines(monkey_lines)
            monkeys[monkey_nbr] = [items, operation, divisor, next_monkey_true, next_monkey_false]
            monkey_lines = []
    return monkeys

def main():
    filename = 'input.txt'
    with open(filename, 'r') as f:
        input = f.readlines()

    m_sim = MonkeySimulation()

    monkeys = parse_input(input)
    for nbr in monkeys:
        m_sim.add_monkey(Monkey(nbr, monkeys[nbr][0], monkeys[nbr][1], monkeys[nbr][2], monkeys[nbr][3], monkeys[nbr][4]))

    nbr_rounds = 20
    for round in range(nbr_rounds):
        #print(round)
        m_sim.iterate_round()

    insp, monkey_business = m_sim.compute_monkey_business()
    print('Answer part I:',monkey_business)

if __name__ == '__main__':
    main()