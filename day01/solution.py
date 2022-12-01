from os import getenv
import numpy as np


class Solution:

    def __init__(self):
        input_file = open('input.txt', 'r').read()
        self.calorie_count = [np.array(r.split('\n')).astype(int) for r in input_file.split('\n\n')]

    def calculate_calories(self):
        return np.array([a.sum() for a in self.calorie_count])


if __name__ == '__main__':
    sol = Solution()
    match getenv('part'):
        case 'part1': print(np.max(sol.calculate_calories()))
        case 'part2': print(np.sort(sol.calculate_calories())[-3:].sum())
        case _:       exit('Invalid name of environment variable \'part\'')
