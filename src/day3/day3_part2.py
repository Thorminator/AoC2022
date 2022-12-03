alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def priority(char):
    return alphabet.index(char) + 1


result = 0
group = []

for line in open('input.txt', 'r').readlines():
    group.append(line)
    if len(group) == 3:
        rucksacks = [set(r.strip()) for r in group]
        common = rucksacks[0].intersection(rucksacks[1]).intersection(rucksacks[2])
        for c in common:
            result += priority(c)
        group.clear()

print(result)
