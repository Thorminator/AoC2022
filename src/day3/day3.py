alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

result = 0

for line in open('input.txt', 'r').readlines():
    middle = len(line) // 2
    r1, r2 = line[middle:], line[:middle]
    for c in set(r1):
        if c in r2:
            result += alphabet.index(c) + 1
            
print(result)
