import math


class Node:
    def __init__(self, char, neighbours, height, start, end):
        self.char = char
        self.distance = 0 if start else math.inf
        self.neighbours = set(neighbours)
        self.height = height
        self.start = start
        self.end = end
        self.visited = False

    def add_neighbours(self, new_neighbours):
        self.neighbours = self.neighbours.union(set(new_neighbours))
