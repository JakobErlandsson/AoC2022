from os import getenv
from itertools import count


def three_above(x, y):
    return (x-1, y-1), (x, y-1), (x+1, y-1)


class Solution:

    def __init__(self):
        self.rock_slices = [i.split(' -> ') for i in open("input.txt", 'r').read().split('\n')]
        self.rock_map = set()
        self.sand_map = set()
        for r in self.rock_slices:
            for i in range(len(r)-1):
                start = list(map(int, r[i].split(',')))
                end = list(map(int, r[i+1].split(',')))
                if start[0] == end[0]:
                    for j in range(min(start[1], end[1]), max(start[1], end[1])+1):
                        self.rock_map.add((start[0], j))
                else:
                    for j in range(min(start[0], end[0]), max(start[0], end[0])+1):
                        self.rock_map.add((j, start[1]))
        self.high_y = max([r[1] for r in self.rock_map])
        if getenv('part') == 'part2':
            self.high_y += 2
            self.unreachable = set()

    def drop_sand(self):
        sand_pos = (500, 0)
        new_pos = self.move(sand_pos)
        while sand_pos != new_pos:
            sand_pos = new_pos
            new_pos = self.move(sand_pos)
            if new_pos[1] > self.high_y:
                return False
        self.sand_map.add(sand_pos)
        return True

    def find_reachable(self):
        num = 0
        for y in range(self.high_y):
            for x in range(500-y, 500+y+1):
                if all(t in self.rock_map or t in self.unreachable for t in three_above(x, y)):
                    self.unreachable.add((x, y))
                else:
                    if (x, y) not in self.rock_map:
                        num += 1
        return num

    def move(self, pos):
        if (pos[0], pos[1] + 1) not in self.rock_map.union(self.sand_map):
            return pos[0], pos[1] + 1
        elif (pos[0] - 1, pos[1] + 1) not in self.rock_map.union(self.sand_map):
            return pos[0] - 1, pos[1] + 1
        elif (pos[0] + 1, pos[1] + 1) not in self.rock_map.union(self.sand_map):
            return pos[0] + 1, pos[1] + 1
        else:
            return pos


if __name__ == '__main__':
    sol = Solution()
    if getenv('part') == 'part1':
        for i in count():
            if not sol.drop_sand():
                break
        print(i)
    if getenv('part') == 'part2':
        print(sol.find_reachable())



