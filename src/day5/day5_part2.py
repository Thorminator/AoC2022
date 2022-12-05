import re

crate_lines = []
move_lines = []

for line in open('input.txt', 'r').read().splitlines():
    if re.search(r'\[\w]', line):
        crate_lines.append(line)
    elif re.search(r'move \d* from \d* to \d*', line):
        move_lines.append(line)


def next_char(index):
    return index * 4 + 1


crates = []

for line in crate_lines:
    i = 0
    while next_char(i) <= len(line):
        next_crate = line[next_char(i)]
        if next_crate == ' ':
            if len(crates) <= i:
                crates.append([])
            i += 1
            continue
        elif len(crates) > i:
            crates[i].append(next_crate)
        else:
            crates.append([next_crate])
        i += 1

for line in move_lines:
    matcher = re.search(r'move (\d*) from (\d*) to (\d*)', line)
    amount, move_from, move_to = [int(matcher.group(i)) for i in range(1, 4)]
    crates_to_move = crates[move_from-1][0:amount]
    crates[move_from-1] = crates[move_from-1][amount:]
    crates[move_to-1] = crates_to_move + crates[move_to-1]
    
print(''.join([x[0] for x in crates]))
