calories = []
calorie_count = 0
for line in open('input.txt', 'r').readlines():
    if len(line.strip()) > 0:
        calorie_count += int(line)
    else:
        calories.append(calorie_count)
        calorie_count = 0
calories.sort(reverse=True)
print(sum(calories[:3]))
