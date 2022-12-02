from os import getenv


class Solution:

    def __init__(self):
        self.symbol_scores = {
            'X': 0,  # Rock / loss
            'Y': 1,  # Paper / draw
            'Z': 2   # Scissors / win
        }
        self.opponent_table = {
            'A': 'X',
            'B': 'Y',
            'C': 'Z'
        }
        self.results = {  # In the order [win, draw, lose] from players POV
            'A': ['Z', 'X', 'Y'],
            'B': ['X', 'Y', 'Z'],
            'C': ['Y', 'Z', 'X']
        }
        self.winning_combinations = [('X', 'C'), ('Y', 'A'), ('Z', 'B')]

        input_file = open("input.txt", 'r').read()
        self.strategy_guide = [i.split(' ') for i in input_file.split('\n')]

    def part2(self):
        score = 0
        for row in self.strategy_guide:
            (opponent, result) = (row[0], row[1])
            hand = self.results[opponent][self.symbol_scores[result]]
            score += self.symbol_scores[hand] + 1
            score += self.symbol_scores[result] * 3
        return score

    def calculate_score(self) -> int:
        score = 0
        for row in self.strategy_guide:
            (opponent, hand) = (row[0], row[1])
            score += self.symbol_scores[hand] + 1
            if hand == self.opponent_table[opponent]:  # Draw
                score += 3
            elif (hand, opponent) in self.winning_combinations:  # Win
                score += 6
        return score


if __name__ == '__main__':
    sol = Solution()
    match getenv('part'):
        case 'part1': print(sol.calculate_score())
        case 'part2': print(sol.part2())
        case _:       exit('Invalid name of environment variable \'part\'')

