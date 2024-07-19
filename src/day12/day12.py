import math

from src.day12.node import Node

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


def get_height_char_from_grid_char(char):
    if char == 'S':
        return 'a'
    elif char == 'E':
        return 'z'
    else:
        return char


def get_neighbours(node_grid, i, j):
    self = node_grid[i][j]
    column_neighbours = node_grid[i][max(0, j - 1):j + 2]
    row_neighbours = [row[j] for row in node_grid[max(0, i - 1):i + 2]]
    neighbours = set(row_neighbours + column_neighbours)
    neighbours.remove(self)
    return neighbours


def create_graph_from_grid(grid):
    all_nodes = []
    node_grid = [[] for _ in grid]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            char = grid[i][j]
            start = char == 'S'
            end = char == 'E'
            node = Node(char, [], ALPHABET.find(get_height_char_from_grid_char(char)), start, end)
            all_nodes.append(node)
            node_grid[i].append(node)
    for i in range(len(node_grid)):
        for j in range(len(node_grid[i])):
            node = node_grid[i][j]
            potential_neighbours = get_neighbours(node_grid, i, j)
            node.add_neighbours([n for n in potential_neighbours if n.height <= node.height + 1])
    return all_nodes


def main():
    grid = []
    for line in open('input.txt', 'r').read().splitlines():
        grid.append([c for c in line])
    nodes = create_graph_from_grid(grid)
    nodes.sort(key=lambda node: node.distance)
    next_node = nodes[0]
    while len(nodes) > 0 and (not next_node.end and not next_node.distance == math.inf):
        next_node = nodes[0]
        new_distance = next_node.distance + 1
        for neighbour in next_node.neighbours:
            if neighbour.visited:
                continue
            if new_distance < neighbour.distance:
                neighbour.distance = new_distance
        next_node.visited = True
        nodes.remove(next_node)
        nodes.sort(key=lambda node: node.distance)
    print(next_node.distance)


if __name__ == '__main__':
    main()
