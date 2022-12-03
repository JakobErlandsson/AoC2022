from os import getenv


class Solution:

    def __init__(self):
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'

        input_file = open('input.txt', 'r').read()
        self.contents = input_file.split('\n')

    def get_priority(self, common):
        score = self.alphabet.index(common.lower()) + 1
        return score if common.islower() else score + 26

    def calc(self):
        sum = 0
        for cont in self.contents:
            l = len(cont) // 2
            common = set(cont[:l]).intersection(cont[l:]).pop()
            sum += self.get_priority(common)
        return sum

    def calc2(self):
        sum = 0
        for i in range(0, len(self.contents), 3):
            (a, b, c) = self.contents[i:i+3]
            common = set(a).intersection(b, c).pop()
            sum += self.get_priority(common)
        return sum


if __name__ == '__main__':
    sol = Solution()
    match getenv('part'):
        case 'part1': print(sol.calc())
        case 'part2': print(sol.calc2())
        case _:       exit('Invalid name of environment variable \'part\'')
