def is_visible(grid, x, y):
    if x == 0 or x == len(grid[x]) - 1 or y == 0 or y == len(grid) - 1:
        return True
    blocked_by = 0
    current_tree = grid[x][y]
    for tree in grid[x][0:y]:
        if tree >= current_tree:
            blocked_by += 1
            break
    for tree in grid[x][y+1:len(grid[x])]:
        if tree >= current_tree:
            blocked_by += 1
            break
    for tree in [row[y] for row in grid[0:x]]:
        if tree >= current_tree:
            blocked_by += 1
            break
    for tree in [row[y] for row in grid[x+1:len(grid)]]:
        if tree >= current_tree:
            blocked_by += 1
            break
    return blocked_by < 4


if __name__ == '__main__':
    lines = open('input.txt', 'r').read().splitlines()
    grid = []
    for line in lines:
        grid.append([int(c) for c in line])
    visible = sum(len(row) for row in grid)
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if not(is_visible(grid, x, y)):
                visible -= 1
    print(visible)
