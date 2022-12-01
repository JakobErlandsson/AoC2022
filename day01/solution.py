from os import getenv


class Solution:

    def __init__(self):
        input_file = open("input.txt", 'r').read()
        self.input_numbers = input_file.split('\n')

    def run(self) -> list[int]:
        sums = []
        sum = 0
        for i in self.input_numbers:
            if i == '':
                sums.append(sum)
                sum = 0
            else:
                sum += int(i)
        return sums


if __name__ == '__main__':
    sol = Solution()
    if getenv('part') == 'part1':
        print(max(sol.run()))
    else:
        print(sum(sorted(sol.run())[-3:]))
