import re

from src.day11.math_evaluator import parse_operation
from src.day11.monkey import Monkey
from src.day11.predicate import parse_predicate


def parse_monkey(monkey):
    items = [item for item in map(int, re.findall(r'(\d+)', monkey[1]))]
    operation = parse_operation(re.match('\s*Operation:\s(.*)', monkey[2]).group(1))
    test = parse_predicate(monkey[3:len(monkey)])
    return Monkey(items, operation, test)


def main(file_name):
    monkey_lines = get_monkey_lines_from_file(file_name)
    monkeys = [parse_monkey(monkey) for monkey in monkey_lines]
    for r in range(20):
        for monkey in monkeys:
            for item in monkey.inspect_all_items():
                new_worry = monkey.operation(item) // 3
                new_monkey = monkey.test.monkey_from_value(new_worry)
                monkeys[new_monkey].items.append(new_worry)
    #     for i, monkey in enumerate(monkeys):
    #         print(f'Monkey {i}: {monkey.items}')
    # for i, monkey in enumerate(monkeys):
    #     print(f'Monkey {i}: inspected items {monkey.inspected} times.')
    monkeys.sort(key=lambda m: m.inspected, reverse=True)
    print(f'{monkeys[0].inspected * monkeys[1].inspected}')


def get_monkey_lines_from_file(file_name):
    monkey_lines = []
    current_monkey_lines = []
    for line in open(file_name, 'r').read().splitlines():
        if line:
            current_monkey_lines.append(line)
        else:
            monkey_lines.append(current_monkey_lines)
            current_monkey_lines = []
    monkey_lines.append(current_monkey_lines)
    return monkey_lines


if __name__ == '__main__':
    main('input.txt')
