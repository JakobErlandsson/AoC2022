from os import getenv


class Solution:

    def __init__(self):
        self.data = open('input.txt', 'r').read()

    def find_unique_string_of(self, n):
        for i in range(len(self.data)-n):
            if set(self.data[i:i+n]).__len__() == n:
                return i+n


if __name__ == '__main__':
    sol = Solution()
    if getenv('part') == 'part1':
        print(sol.find_unique_string_of(4))
    if getenv('part') == 'part2':
        print(sol.find_unique_string_of(14))

