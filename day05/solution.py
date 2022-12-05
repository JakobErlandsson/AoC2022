from os import getenv


class Solution:

    def __init__(self):
        input_file = open('input.txt', 'r').read()
        (self.start, self.procedure) = input_file.split('\n\n')
        self.stacks = {}
        for row in self.start.split('\n'):
            crates = [i for i,x in enumerate(row) if x == '[']
            for c in crates:
                if c//4 in self.stacks.keys():
                    self.stacks[c//4].append(row[c+1])
                else:
                    self.stacks[c//4] = [row[c+1]]
        self.stacks = {k: list(reversed(self.stacks[k])) for k in self.stacks}

    def do_procedure(self, part):
        for step in self.procedure.split('\n'):
            step = step.split(' ')
            n_crates = int(step[1])
            from_stack = self.stacks[int(step[3])-1]
            to_stack = self.stacks[int(step[5])-1]

            if part == 'part1':
                to_stack.extend(reversed(from_stack[-n_crates:]))
            if part == 'part2':
                to_stack.extend(from_stack[-n_crates:])
                
            del from_stack[-n_crates:]


if __name__ == '__main__':
    sol = Solution()
    sol.do_procedure(getenv('part'))
    print(''.join([sol.stacks[s].pop() for s in range(sol.stacks.__len__())]))
