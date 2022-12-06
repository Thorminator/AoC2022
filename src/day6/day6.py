data = open('input.txt', 'r').read().strip()
distinct_chars_to_find = 4
for i in range(len(data)):
    chars = set(data[i:i + distinct_chars_to_find])
    if len(chars) == distinct_chars_to_find:
        print(i + distinct_chars_to_find)
        break
