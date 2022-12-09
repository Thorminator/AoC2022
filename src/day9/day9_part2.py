import re
from itertools import repeat


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


def follow(tx, ty, fx, fy):
    dx, dy = fx - tx, fy - ty
    move_x = dx / abs(dx) if dx != 0 else 0
    move_y = dy / abs(dy) if dy != 0 else 0
    if abs(dx) <= 1 and abs(dy) <= 1:
        return tx, ty
    else:
        return tx + move_x, ty + move_y


def main():
    hx, hy = (0, 0)
    tails = [tail for tail in repeat((0, 0), 9)]
    visited = {0, 0}
    for line in open('input.txt', 'r').read().splitlines():
        match = re.match(r'(\w) (\d+)', line)
        direction = match.group(1)
        length = int(match.group(2))
        while length > 0:
            hx, hy = move_head(direction, hx, hy)
            for i, tail in enumerate(tails):
                tx, ty = tail
                fx, fy = tails[i - 1] if i > 0 else (hx, hy)
                old_tx, old_ty = tx, ty
                tx, ty = follow(tx, ty, fx, fy)
                if old_tx == tx and old_ty == ty:
                    break
                else:
                    tails[i] = (tx, ty)
                if i == len(tails) - 1:
                    visited.add((tx, ty))
            length -= 1
    print(len(visited))


if __name__ == '__main__':
    main()
