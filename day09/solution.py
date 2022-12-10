from os import getenv


def is_attached(k1, k2):
    return k1.dist_to(k2) <= 1


class Snake:

    def __init__(self, tail_length):
        self.head = Direction(0, 0)
        self.tail = [Direction(0, 0) for _ in range(tail_length)]
        self.tail_positions = {(self.tail[-1].x, self.tail[-1].y)}

    def move(self, direction):
        match direction[0]:
            case 'U':
                way = Direction(0, -1)
            case 'D':
                way = Direction(0, 1)
            case 'L':
                way = Direction(-1, 0)
            case 'R':
                way = Direction(1, 0)
        for _ in range(int(direction[1])):
            self.head.add(way)
            knot_ahead = self.head
            for t in self.tail:
                if not is_attached(t, knot_ahead):
                    to_move = Direction(0, 0)
                    to_move.x = max(-1, min(1, knot_ahead.x - t.x))
                    to_move.y = max(-1, min(1, knot_ahead.y - t.y))
                    t.add(to_move)
                knot_ahead = t
            self.tail_positions.add((self.tail[-1].x, self.tail[-1].y))


class Direction:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def add(self, other):
        self.x += other.x
        self.y += other.y

    def dist_to(self, other):
        dx = abs(self.x - other.x)
        dy = abs(self.y - other.y)
        return max(dx, dy)


class Solution:

    def __init__(self, tail_length):
        input = open('input.txt').read().split('\n')
        self.directions = [i.split(' ') for i in input]
        self.snake = Snake(tail_length)

    def run(self):
        for line in self.directions:
            self.snake.move(line)


if __name__ == '__main__':
    match (getenv('part')):
        case 'part1':
            sol = Solution(1)
        case 'part2':
            sol = Solution(9)
    sol.run()
    print(len(list(sol.snake.tail_positions)))






