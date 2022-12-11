from os import getenv


class Solution:

    def __init__(self):
        self.instructions = [i.split(' ') for i in open("input.txt", 'r').read().split('\n')]
        self.x = 1
        self.cycle_count = 0
        self.breakpoints = [20, 60, 100, 140, 180, 220]
        self.breakpoints2 = [39, 79, 119, 159, 199, 239]

    def run(self):
        row = ''
        for inst in self.instructions:
            if self.cycle_count % 40 in (self.x-1, self.x, self.x+1):
                row += '#'
            else:
                row += '.'
            if getenv('part') == 'part1' and self.cycle_count in self.breakpoints:
                yield self.x * self.cycle_count
            if getenv('part') == 'part2' and self.cycle_count in self.breakpoints2:
                yield row
                row = ''
            self.cycle_count += 1
            if inst[0] != 'noop':
                if self.cycle_count % 40 in (self.x - 1, self.x, self.x + 1):
                    row += '#'
                else:
                    row += '.'
                if getenv('part') == 'part1' and self.cycle_count in self.breakpoints:
                    yield self.x * self.cycle_count
                if getenv('part') == 'part2' and self.cycle_count in self.breakpoints2:
                    yield row
                    row = ''
                self.cycle_count += 1
                self.x += int(inst[1])


if __name__ == '__main__':
    sol = Solution()
    match getenv('part'):
        case 'part1':
            print(sum(sol.run()))
        case 'part2':
            print('\n'.join(sol.run()))
        case _:       exit('Invalid name of environment variable \'part\'')

