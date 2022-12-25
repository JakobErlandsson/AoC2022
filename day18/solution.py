from os import getenv
from collections import deque


def get_sides(cube):
    (x, y, z) = cube
    return [(x+1, y, z), (x-1, y, z), (x, y+1, z),
            (x, y-1, z), (x, y, z+1), (x, y, z-1)]


class Solution:

    def __init__(self):
        self.cubes = [c.split(',') for c in open("input.txt", 'r').read().split('\n')]
        self.cubes = set((int(x), int(y), int(z)) for (x, y, z) in self.cubes)
        self.max_x = max([x[0] for x in self.cubes])
        self.max_y = max([x[1] for x in self.cubes])
        self.max_z = max([x[2] for x in self.cubes])

    def find_surface_area(self):
        return sum([len([s for s in get_sides(c) if s not in self.cubes]) for c in self.cubes])

    def search_entire_space(self):
        queue = deque()
        visited = {(-1, -1, -1)}
        queue.append((-1, -1, -1))
        sides = {}
        while queue:
            v = queue.popleft()
            all_sides = get_sides(v)
            inside = [a for a in all_sides if self.inside_space(a)]
            blocked = [a for a in inside if a in self.cubes]
            for b in blocked:
                if b in sides:
                    sides[b].add(v)
                else:
                    sides[b] = {v}
            for n in [i for i in inside if i not in self.cubes]:
                if n not in visited:
                    visited.add(n)
                    queue.append(n)
        return sides

    def inside_space(self, cube):
        (x, y, z) = cube
        return self.max_x + 1 >= x >= -1 and self.max_y + 1 >= y >= -1 and self.max_z + 1 >= z >= -1


if __name__ == '__main__':
    sol = Solution()
    if getenv('part') == 'part1':
        print(sol.find_surface_area())
    else:
        print(sum([len(v) for v in sol.search_entire_space().values()]))

