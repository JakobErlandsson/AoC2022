from os import getenv
from collections import deque


class Solution:

    def __init__(self):
        self.input_file = [list(i) for i in open("input.txt", 'r').read().split('\n')]
        (self.rows, self.cols) = (len(self.input_file), len(self.input_file[0]))
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.mountain_map = {(x, y): self.input_file[y][x] for y in range(self.rows) for x in range(self.cols)}
        self.start = list(self.mountain_map.keys())[list(self.mountain_map.values()).index('S')]
        self.end = list(self.mountain_map.keys())[list(self.mountain_map.values()).index('E')]
        self.mountain_map[self.start] = 'a'
        self.mountain_map[self.end] = 'z'
        self.climbing_map = {(x, y): self.get_climbable_neighbours(x, y) for (x, y) in self.mountain_map.keys()}

    def get_climbable_neighbours(self, x, y):
        ns = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        if x == 0: ns.remove((x - 1, y))
        if y == 0: ns.remove((x, y - 1))
        if x == self.cols - 1: ns.remove((x + 1, y))
        if y == self.rows - 1: ns.remove((x, y + 1))
        height = self.alphabet.index(self.mountain_map[(x, y)])
        return [n for n in ns if self.alphabet.index(self.mountain_map[n]) + 1 >= height]

    def breadth_first(self, source):
        queue = deque()
        parents = {k: None for k in self.mountain_map.keys()}
        visited = {source}
        queue.append(source)
        while queue:
            v = queue.popleft()
            if getenv('part') == 'part2' and self.mountain_map[v] == 'a':
                return v, parents
            if getenv('part') == 'part1' and v == self.start:
                return v, parents
            for neighbour in self.climbing_map[v]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    parents[neighbour] = v
                    queue.append(neighbour)


if __name__ == '__main__':
    sol = Solution()
    start, path = sol.breadth_first(sol.end)
    length = 0
    while path[start]:
        length += 1
        start = path[start]
    print(length)


