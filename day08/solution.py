from os import getenv
from math import prod


def get_neighbours(size):
    neighbour_map = {}
    for y in range(1, size-1):
        for x in range(1, size-1):
            left = [(i, y) for i in range(x)]
            right = [(i, y) for i in range(x+1, size)]
            up = [(x, j) for j in range(y)]
            down = [(x, j) for j in range(y+1, size)]
            neighbour_map[(x, y)] = [left, right, up, down]

    return neighbour_map


class Solution:

    def __init__(self):
        trees = [list(map(int, list(l))) for l in open('input.txt', 'r').read().split('\n')]
        self.size = len(trees)
        self.tree_map = {(x, y): trees[y][x] for x in range(self.size) for y in range(self.size)}
        self.neighbours = {}

    def look_from_outside(self):
        seen = 0
        self.neighbours = get_neighbours(self.size)
        for y in range(self.size):
            for x in range(self.size):
                if y in (0, self.size-1) or x in (0, self.size-1):
                    seen += 1
                else:
                    neighbours = self.neighbours[(x, y)]
                    if any(all(self.tree_map[h] < self.tree_map[(x, y)] for h in n) for n in neighbours):
                        seen += 1
        return seen

    def find_scenic_score(self, x, y):
        height = self.tree_map[(x, y)]
        seen_list = []
        seen = 0

        # Look up (decrease y)
        for i in range(y-1, -1, -1):
            seen += 1
            tree = self.tree_map[(x, i)]
            if tree >= height:
                break
        seen_list.append(seen)
        seen = 0
        # Look left (decrease x)
        for i in range(x-1, -1, -1):
            seen += 1
            tree = self.tree_map[(i, y)]
            if tree >= height:
                break
        seen_list.append(seen)
        seen = 0
        # Look down (increase y)
        for i in range(y+1, self.size):
            seen += 1
            tree = self.tree_map[(x, i)]
            if tree >= height:
                break
        seen_list.append(seen)
        seen = 0
        # Look right (increase x)
        for i in range(x+1, self.size):
            seen += 1
            tree = self.tree_map[(i, y)]
            if tree >= height:
                break
        seen_list.append(seen)

        return prod(seen_list)


if __name__ == '__main__':
    sol = Solution()
    match (getenv('part')):
        case 'part1':
            print(sol.look_from_outside())
        case 'part2':
            scores = [sol.find_scenic_score(x, y) for y in range(1, sol.size-1) for x in range(1, sol.size-1)]
            print(max(scores))






