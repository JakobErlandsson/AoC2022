from os import getenv


class Solution:

    def __init__(self):
        input_file = open("input.txt", 'r').read()
        self.calorie_count = [map(int, r.split('\n')) for r in input_file.split('\n\n')]

    def calculate_calories(self) -> list[int]:
        return [sum(cals) for cals in self.calorie_count]


if __name__ == '__main__':
    sol = Solution()
    match getenv('part'):
        case 'part1': print(max(sol.calculate_calories()))
        case 'part2': print(sum(sorted(sol.calculate_calories())[-3:]))
        case _:       exit('Invalid name of environment variable \'part\'')
