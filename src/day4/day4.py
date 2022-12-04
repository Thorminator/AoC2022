def get_interval(interval_text):
    limits = interval_text.split('-')
    return int(limits[0]), int(limits[1])


pairs = []
result = 0
for line in open('input.txt', 'r').readlines():
    pair = line.split(',')
    l1, u1 = get_interval(pair[0])
    l2, u2 = get_interval(pair[1])
    if (l1 <= l2 and u1 >= u2) or (l2 <= l1 and u2 >= u1):
        result += 1
print(result)
