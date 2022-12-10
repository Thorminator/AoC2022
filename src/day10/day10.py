import re

INSTRUCTION_CYCLES = {
    'addx': 2,
    'noop': 1
}

COMPLETION_FUNCTION = {
    'noop': lambda x, arg: x,
    'addx': lambda x, arg: x + arg
}


def main():
    cycle = 0
    x = 1
    signal_strength_sum = 0
    for line in open('input.txt', 'r').read().splitlines():
        match = re.match(r'(\w+)\s?(-?\d+)?', line)
        instruction = match.group(1)
        arg = int(match.group(2)) if match.group(2) else None
        cycles_to_complete = INSTRUCTION_CYCLES[instruction]
        completion_function = COMPLETION_FUNCTION[instruction]
        while cycles_to_complete > 0:
            cycle += 1
            cycles_to_complete -= 1
            if (cycle - 20) % 40 == 0:
                signal_strength = cycle * x
                signal_strength_sum += signal_strength
                print(f'Cycle {cycle}, X: {x}, signal strength: {signal_strength}')
        x = completion_function(x, arg)
    print(signal_strength_sum)

if __name__ == '__main__':
    main()
