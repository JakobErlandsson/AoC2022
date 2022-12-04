from os import getenv


class Solution:

    def __init__(self):
        input_file = open('input.txt', 'r').read()
        input_file = [a.split(',') for a in input_file.split('\n')]
        self.pairs = []
        for (elf1, elf2) in input_file:
            elf1 = [int(a) for a in elf1.split('-')]
            elf2 = [int(a) for a in elf2.split('-')]
            self.pairs.append((elf1, elf2))

    def calc(self, part: str) -> int:
        num = 0
        for (elf1, elf2) in self.pairs:
            ranges = (range(elf1[0], elf1[1]+1), range(elf2[0], elf2[1]+1))
            inter = set(ranges[0]).intersection(ranges[1])
            if part == 'part1' and inter.__len__() in map(len, ranges):
                num += 1
            if part == 'part2' and inter:
                num += 1
        return num


if __name__ == '__main__':
    sol = Solution()
    print(sol.calc(getenv('part')))
