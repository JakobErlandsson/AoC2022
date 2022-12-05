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
    if getenv('part') == 'part1':
        print(np.max(sol.calculate_calories()))
    elif getenv('part') == 'part2':
        sum = 0
        result = sol.calculate_calories()
        for _ in range(3):
            highest = result.max()
            result = np.setdiff1d(result, highest)
            sum += highest
        print(sum)
    else:
        exit('Invalid name of environment variable \'part\'')
