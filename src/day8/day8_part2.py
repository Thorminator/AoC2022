from functools import reduce


def scenic_score(grid, x, y):
    if x == 0 or x == len(grid[x]) - 1 or y == 0 or y == len(grid) - 1:
        return 0
    scenic_scores = [0, 0, 0, 0]
    current_tree = grid[x][y]
    for tree in grid[x][0:y].__reversed__():
        scenic_scores[0] += 1
        if tree >= current_tree:
            break
    for tree in grid[x][y + 1:len(grid[x])]:
        scenic_scores[1] += 1
        if tree >= current_tree:
            break
    for tree in [row[y] for row in grid[0:x]].__reversed__():
        scenic_scores[2] += 1
        if tree >= current_tree:
            break
    for tree in [row[y] for row in grid[x + 1:len(grid)]]:
        scenic_scores[3] += 1
        if tree >= current_tree:
            break
    return reduce(lambda a, b: a * b, scenic_scores)


if __name__ == '__main__':
    lines = open('input.txt', 'r').read().splitlines()
    grid = []
    for line in lines:
        grid.append([int(c) for c in line])
    scores = []
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            scores.append(scenic_score(grid, x, y))
    print(max(scores))
