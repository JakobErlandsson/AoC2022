from os import getenv
import re


def dist(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])


class Solution:

    def __init__(self):
        self.input_txt = [list(map(int, re.findall(r'-*\d+', i))) for i in open("input.txt", 'r').read().split('\n')]
        self.row_to_test = 2000000
        self.max_dimension = 4000000
        self.sensors = {(i[0], i[1]): (i[2], i[3]) for i in self.input_txt}
        self.distances = {i: dist(i, self.sensors[i]) for i in self.sensors}
        self.seen_beacons = set(self.sensors.values())
        self.no_beacons = set()
        self.not_empty = set()

    def get_border(self, point, distance):
        point1 = (point[0] + distance + 1, point[1])
        point2 = (point[0] - distance - 1, point[1])
        point3 = point1
        point4 = point2
        border = {point1, point2, (point[0], point[1] + distance + 1), (point[0], point[1] - distance - 1)}
        for _ in range(distance):
            point1 = (point1[0] - 1, point1[1] + 1)
            point2 = (point2[0] + 1, point2[1] + 1)
            point3 = (point3[0] - 1, point3[1] - 1)
            point4 = (point4[0] + 1, point4[1] - 1)
            border.update([point1, point2, point3, point4])
        return {p for p in border if 0 <= p[0] <= self.max_dimension and 0 <= p[1] <= self.max_dimension}

    def calc_no_beacons(self):
        for s in self.sensors:
            d = dist(s, self.sensors[s])
            y_range = range(s[1]-d, s[1]+d)
            if self.row_to_test in y_range:
                if s[1] < self.row_to_test:
                    dist_to_check = y_range.stop - self.row_to_test
                else:
                    dist_to_check = self.row_to_test - y_range.start
                x_range = range(s[0] - dist_to_check, s[0] + dist_to_check + 1)
                self.no_beacons.update({i for i in x_range})
        self.no_beacons.difference_update({b[0] for b in self.seen_beacons if b[1] == self.row_to_test})

    def find_missing_spot(self):
        for s in self.sensors:
            d = dist(s, self.sensors[s])
            border = [b for b in self.get_border(s, d) if b not in self.not_empty]
            for p in border:
                distance_to_sensors = {s: dist(p, s) for s in self.sensors}
                if all(distance_to_sensors[x] > self.distances[x] for x in self.sensors):
                    return p
                else:
                    self.not_empty.add(p)


if __name__ == '__main__':
    sol = Solution()
    if getenv('part') == 'part1':
        sol.calc_no_beacons()
        print(len(sol.no_beacons))
    else:
        point = sol.find_missing_spot()
        print(point[0] * 4000000 + point[1])



