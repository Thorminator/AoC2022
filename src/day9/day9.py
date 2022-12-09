import re


def move_head(direction, hx, hy):
    x, y = get_direction_vector(direction)
    return hx + x, hy + y


def get_direction_vector(direction):
    if direction == 'R':
        return 1, 0
    elif direction == 'L':
        return -1, 0
    elif direction == 'U':
        return 0, 1
    else:
        return 0, -1


def print_grid(tx, ty, hx, hy):
    for y in range(5).__reversed__():
        print('')
        for x in range(6):
            if x == hx and y == hy:
                print(' H ', end='')
            elif x == tx and y == ty:
                print(' T ', end='')
            else:
                print(' . ', end='')
    print('')


def print_visited(visited):
    for y in range(5).__reversed__():
        print('')
        for x in range(6):
            if (x, y) in visited:
                print(' # ', end='')
            else:
                print(' . ', end='')
    print('')


def follow_head(tx, ty, hx, hy):
    dx, dy = hx - tx, hy - ty
    move_x = dx / abs(dx) if dx != 0 else 0
    move_y = dy / abs(dy) if dy != 0 else 0
    if abs(dx) <= 1 and abs(dy) <= 1:
        return tx, ty
    else:
        return tx + move_x, ty + move_y


def main(do_print):
    tx, ty, hx, hy = (0, 0, 0, 0)
    if do_print:
        print_grid(tx, ty, hx, hy)
    visited = set()
    for line in open('test.txt', 'r').read().splitlines():
        match = re.match(r'(\w) (\d+)', line)
        direction = match.group(1)
        length = int(match.group(2))
        while length > 0:
            hx, hy = move_head(direction, hx, hy)
            tx, ty = follow_head(tx, ty, hx, hy)
            visited.add((tx, ty))
            length -= 1
            if do_print:
                print_grid(tx, ty, hx, hy)
    if do_print:
        print_visited(visited)
    print(len(visited))


if __name__ == '__main__':
    main(True)
